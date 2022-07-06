from google.cloud import translate
from decouple import config


def translate_text(
    text: str = "YOUR_TEXT_TO_TRANSLATE",
    target_language_code: str = "",
    lss: list = [],
    i: int = 0,
):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{config('GOOGLE_PROJECT_ID')}/locations/{location}"

    try:
        source_language_code = detect_language(client=client,
                                               parent=parent,
                                               text=text)
    except Exception as e:
        return {'error': e.message}

    if target_language_code == source_language_code:
        return {
            'detect_language': source_language_code,
            'translated_text': text,
            'target_language_code': target_language_code
        }

    try:
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",  # mime types: text/plain, text/html
                "source_language_code": source_language_code,
                "target_language_code": target_language_code,
            })
    except Exception:
        return {
            'detect_language':
            source_language_code,
            'translated_text':
            text,
            'target_language_code':
            source_language_code,
            'error':
            f'Dont have any target_language_code name: {target_language_code}'
        }

    translated_text = None
    # Display the translation for each input text provided
    for translation in response.translations:
        translated_text = translation.translated_text
    lss.append((i, translated_text))
    return {
        'detect_language': source_language_code,
        'translated_text': translated_text,
        'target_language_code': target_language_code
    }


def detect_language(client: translate.TranslationServiceClient(),
                    parent: str,
                    text: str = "Hello, world!"):
    """Detecting the language of a text string."""

    # https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
        content=text,
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )
    language_code = None
    # Display list of detected languages sorted by detection confidence.
    # The most probable language is first.
    for language in response.languages:
        # The language detected
        language_code = language.language_code

    return language_code


def list_languages():
    """Lists all available languages."""
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    results = translate_client.get_languages()

    return {'languages': results}


def split_limit_words(text: str):
    """Limit words in text."""
    text = text.split()
    n = 5300

    return [' '.join(text[i:i + n]) for i in range(0, len(text), n)]


import time


def trans_file():
    start = time.time()
    with open('django_ex/test.txt', 'r') as f:
        txt = f.read()
    data = split_limit_words(txt)

    f = open('django_ex/out1.txt', 'a')
    for txt in data:
        trans = translate_text(txt, 'en')
        f.write(trans['translated_text'])
    f.close()
    end = time.time()
    waste = end - start
    print('TRANS NORMAL WASTE: ', waste)


from threading import Thread


def translate_multithread():
    start = time.time()
    with open('django_ex/test.txt', 'r') as f:
        txt = f.read()
    data = split_limit_words(txt)
    ls = []
    lss = []
    f = open('django_ex/out.txt', 'a')
    for i, t in enumerate(data):
        trans = Thread(target=translate_text, args=(t, 'en', lss, i))
        trans.start()
        time.sleep(5)
        ls.append(trans)

    while True:
        if ls == []:
            break
        for i in ls:
            i.join()
            if i.is_alive():
                continue
            ls.remove(i)
    sorted_lss = sorted(lss, key=lambda tup: tup[0])
    for i in sorted_lss:
        f.write(i[1])
    f.close()
    end = time.time()
    waste = end - start
    print('TRANS MULTITHREAD WASTE: ', waste)
    pass
