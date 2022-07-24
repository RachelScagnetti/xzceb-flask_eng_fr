"""Work with Watson Translator API"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/dafffe6c-acb7-4f34-8450-3ea60877a3d4')

def english_to_french(textToTranslate):
    """English to French translation"""
    response = language_translator.translate(
        text=textToTranslate,
        model_id='en-fr').get_result()
    translated_text = response['translations'][0]['translation']
    return translated_text

def french_to_english(textToTranslate):
    """French to English translation"""
    response = language_translator.translate(
        text=textToTranslate,
        model_id='fr-en').get_result()
    translated_text = response['translations'][0]['translation']
    return translated_text
