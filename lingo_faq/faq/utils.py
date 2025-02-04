def filter_by_language(data, lang):
    """
    Utility method to filter FAQs by the specified language.
    """
    output_data = []
    for faq in data:
        if lang in faq["translations"]:
            faq["translations"] = {lang: faq["translations"][lang]}
            output_data.append(faq)
    return output_data
