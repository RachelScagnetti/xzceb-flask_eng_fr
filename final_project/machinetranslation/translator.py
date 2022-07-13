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

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/dafffe6c-acb7-4f34-8450-3ea60877a3d4')

def englishToFrench(self):
    text='Hello'
    frenchTextTranslation = language_translator.translate(text, 
    model_id='en-fr').get_result()
    return frenchTextTranslation

def frenchToEnglish(frenchText):
    text = 'Bonjour'
    englishTextTranslation = language_translator.translate(text,
    model_id='fr-en').get_result()
    return englishTextTranslation