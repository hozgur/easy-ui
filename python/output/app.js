
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('from_server', function(data) {
    if(data.event_name == "init"){
        var myapp = document.getElementById(data.id);
        myapp.innerHTML = data.value;
    }
    if(data.event_name == "change"){
        var elm = document.getElementById(data.id);
        elm.value = data.value;
    }
});

function clientEmit(id,newValue,event_name) {
    socket.emit('from_client', {id: id, value: newValue, event_name: event_name});
}

window.clientEmit = clientEmit;


window.onload = function () {
    // request the data from the server
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/init', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var data = xhr.responseText;
            // get myapp div
            var myapp = document.getElementById('myapp');
            // set the innerHTML
            myapp.innerHTML = data;
            clientEmit("myapp","init","init")
        }
    }
    xhr.send();
}