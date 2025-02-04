def filter_by_language(data, lang):
    """
    Utility method to filter FAQs by the specified language.
    """
    output_data = []
    for faq in data:
        translations = faq.get("translations", {})  # Default to empty dict if None
        if isinstance(translations, dict) and lang in translations:
            faq["translations"] = {lang: translations[lang]}
            output_data.append(faq)
    return output_data
