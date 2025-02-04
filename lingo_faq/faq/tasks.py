import asyncio
import logging

from celery import shared_task
from googletrans import Translator

from faq.choices import LanguageChoices
from faq.models import FAQ

logger = logging.getLogger(__name__)


def translate_text(question, answer, src, dest):
    """
    Translates the given question and answer from the source language to the destination language.
    Ensures synchronous execution inside Celery.

    Args:
        question (str): The question to be translated.
        answer (str): The answer to be translated.
        src (str): The source language code.
        dest (str): The destination language code.

    Returns:
        dict: A dictionary containing the translated question and answer.
    """
    translator = Translator()

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        question_translation = loop.run_until_complete(
            translator.translate(question, src=src, dest=dest)
        )
        answer_translation = loop.run_until_complete(
            translator.translate(answer, src=src, dest=dest)
        )

        return {
            dest: {
                "question": question_translation.text,
                "answer": answer_translation.text,
            }
        }
    except Exception as e:
        logger.error(f"Error translating to {dest}: {str(e)}")
        return None


@shared_task
def start_translation(obj_id, question, answer, src):
    """
    Asynchronously translates the given question and answer into all available languages
    and updates the corresponding FAQ instance with the new translations.

    Args:
        obj_id (int): The ID of the FAQ instance to be updated.
        question (str): The question text to be translated.
        answer (str): The answer text to be translated.
        src (str): The source language code.

    Returns:
        None
    """
    translated_data = {}

    # Create Celery subtasks for each translation
    tasks = [
        translate_text(question, answer, src, lang[0])
        for lang in LanguageChoices.choices()
    ]

    # Execute tasks asynchronously and collect results
    results = [task for task in tasks]
    for result in results:
        try:
            translated_result = result  # Get the task result
            if translated_result:
                translated_data.update(translated_result)
        except Exception as e:
            logger.error(f"Error retrieving translation task result: {str(e)}")

    logger.info(f"Translated Data: {translated_data}")

    try:
        # Fetch the FAQ instance
        logger.info(f"Saving translations: {translated_data}")
        instance = FAQ.objects.get(id=obj_id)

        # Merge new translations with existing ones
        existing_translations = instance.translations or {}
        existing_translations.update(translated_data)

        # Save the updated translations
        instance.translations = existing_translations
        instance.save()

        logger.info(f"Successfully updated translations for FAQ ID {obj_id}")
    except FAQ.DoesNotExist:
        logger.error(f"FAQ with id {obj_id} does not exist.")
