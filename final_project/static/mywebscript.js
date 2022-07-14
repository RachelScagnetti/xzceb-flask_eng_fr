let english_to_french = ()=>{
    english_text = document.getElementById("english_text").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("english_to_french").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "english_to_french?english_text"+"="+english_text, true);
    xhttp.send();
}

let english_translation = ()=>{
    french_text = document.getElementById("french_text").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("english_translation").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "french_to_english?french_text"+"="+french_text, true);
    xhttp.send();
}

