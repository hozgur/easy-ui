
var socket = io.connect('http://' + document.domain + ':' + location.port);
var viewers = {}
socket.on('from_server', function(data) {
    console.log(data);
    if(data.event_name == "init-content"){
        var myapp = document.getElementById(data.id);
        myapp.innerHTML = data.value;
    }
    if(data.event_name.startsWith("change-")){
        var elm = document.getElementById(data.id);
        elm[data.event_name.split("-")[1]] = data.value;
    }
    
    if(data.event_name == "init-seadragon"){
        viewers[data.id] = OpenSeadragon({
            id: data.id,
            prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
            animationTime: 0
        });
        console.log("init-seadragon");
        console.log(viewers);
    }
    if(data.event_name.startsWith("seadragon-")){
        let command = data.event_name.split("-")[1];
        viewers[data.id][command](data.value);
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