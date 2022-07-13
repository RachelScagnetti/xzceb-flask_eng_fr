import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='{2018-05-01}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    englishText='Test'
    frenchTextTranslation = language_translator.translate(englishText, model_id='en-fr')
    return frenchTextTranslation

def frenchToEnglish(frenchText):
    frenchText = 'Test'
    englishTextTranslation = language_translator.translate(frenchText, model_id='fr-en')
    return englishTextTranslation