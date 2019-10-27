if(localStorage.getItem('sight')){
    sendQuery();


}


document.getElementById("mic").addEventListener('click',startDictation);
document.getElementById("speaker").addEventListener('click',function () {
    sendQuery(getText());
});

function getText(){
    let text = "Exhibition!";
     text+= document.getElementById('name').innerText;
     text+= " !Description";
     text +=document.getElementById('description').innerText;
     let test = document.getElementById('description').innerText;
     return text;
}

function sendQuery(text,callback){
    if(!text || text==""){
            text = getText();
    }

        var request = JSON.stringify({text:text});
        console.log(request);
        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
                var test = atob(this.responseText);
                console.log(test);
                var snd = new Audio("data:audio/mp3;base64," + this.responseText);
                snd.play().then(callback);
            }
            else{
                console.log("No response");
            }
        };
        xhttp.open("POST", "http://localhost:5000/api/tts", true);
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.send(request);
    }


    function startDictation() {

    sendQuery("Please say if you are happy or sad!",function () {
        if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.lang = "en-US";
      recognition.start();

      recognition.onresult = function(e) {
        changeColor(e.results[0][0].transcript);
        recognition.stop();

      };

      recognition.onerror = function(e) {
        recognition.stop();
      }

    }
    });


  }
  function changeColor(text) {
    if(text.includes("sad")){
        document.getElementById("mic").style.backgroundColor = "red";

    }
    else if(text.includes("happy")){
        document.getElementById("mic").style.backgroundColor = "green";
    }

  }
  