
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

        }
    }
    xhr.send();
}