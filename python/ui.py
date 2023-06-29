
from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element, Elm
from components.slider import Slider
from components.button import Button
from components.image import Image
import connection
def onimageclick(id, value):
    print(f"Image {id} clicked")
    img = Elm("img")
    if img is not None:
        img.value = value


def onchangeSlider(id, value):
    print(f"Slider Value of {id} changed to {value}")
    a = Elm("a") if id == "as" else Elm("as")
    if a is not None:
        a.value = value
    with Row(id="imagerow") as imagerow:
        imagerow.cls("container").cls("border").style("flex-wrap:wrap").style("width:100%")
        for i in range(0,int(value)):
            Image(id=f"img{i}",value= f"./image/{i}").on("click", onimageclick)
    connection.send("imagerow", imagerow.render(), "init-content")
 
    

with Element(id="main") as main:
    main.cls("container").style("width:100%").style("height:100%")
    with Row() as row1:
        row1.cls("container").cls("border")
        with Col() as col1:
            col1.cls("w12").cls("border").style("height:50%")
            with Row() as row:
                Label(usefor="a",value="Images:")
                Input(id="a",value="0").on("change", onchangeSlider)
            Slider(id="as",value="0").on("change", onchangeSlider)
        with Col() as col2:
            col2.cls("border").style("height:50%").style("width:auto")
            img = Image(id="img",value="./image/0")
            img.style("width:auto").style("height:500px")
    with Row() as imagerow:
        imagerow.id = "imagerow"
        imagerow.cls("container").cls("border").style("flex-wrap:wrap").style("width:100%")
        for i in range(0,20):
            Image(id=f"img{i}",value= f"./image/{i}").on("click", onimageclick)
            


def UI():
    return main.render()


