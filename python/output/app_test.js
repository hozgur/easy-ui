// define onchange event function
function my_onchange(event) {
    console.log(event);
    console.log("onchange");
    var a = document.getElementById("A").value;
    var b = document.getElementById("B").value;
    var c = parseInt(a) + parseInt(b);
    console.log(c);    
    document.getElementById("result").value = c.toString();
}

window.onload = function () {
    src = {
        url: "image/0",
        type: 'image',
    };
    window.viewer.open(src);
}