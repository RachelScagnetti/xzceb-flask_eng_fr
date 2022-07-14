let translateToFrench = ()=>{
    english_text = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "english_to_french?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
}

let translateToEnglish = ()=>{
    french_text = document.getElementById("french_text").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("english_translation").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "french_to_english?english_translation"+"="+french_text, true);
    xhttp.send();
}

