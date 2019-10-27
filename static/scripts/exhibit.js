if(localStorage.getItem('sight')){
    document.getElementById('disabilities').innerText+="This is friends to visually impaired!"
    var text = "Exhibition!";
     text+= document.getElementById('name').innerText;
     text+= " !Description";
     text +=document.getElementById('description').innerText;
    try {
            sendQuery(text);

} catch(e) {
    console.log(e);
}
}
if(localStorage.getItem('hearing')){
    document.getElementById('disabilities').innerText+="This is friends to hearing impaired!"
}
if(localStorage.getItem('other')){
    document.getElementById('disabilities').innerText+="This is friends to mobility impaired!"
}


function sendQuery(text){


        var request = JSON.stringify({text:text});
        console.log(request);
        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
                var test = atob(this.responseText);
                console.log(test);
                var snd = new Audio("data:audio/mp3;base64," + this.responseText);
                snd.play().catch(function(error){

                });



            }
            else{
                console.log("No response");
            }
        };
        xhttp.open("POST", "http://localhost:5000/api/tts", true);
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.send(request);
    }