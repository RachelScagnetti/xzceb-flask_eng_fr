from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    english_text = request.args.get('textToTranslate')
    # Write your code here
    french_translation = translator.english_to_french(english_text)
    return french_translation

@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_translation = translator.french_to_english(textToTranslate)
    return english_translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
