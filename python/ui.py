from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element, Elm
from components.slider import Slider
from components.button import Button
from components.image import Image
from components.imageviewer import ImageViewer
import connection
def onimageclick(id, value):
    print(f"Image {id} clicked")
    img = Elm("viewer1")
    if img is not None:
        img.value = value


def onchangeSlider(id, value):
    print(f"Slider Value of {id} changed to {value}")
    a = Elm("a") if id == "as" else Elm("as")
    if a is not None:
        a.value = value
    with Row(id="imagerow") as imagerow:
        imagerow.cls("container").cls("border").style("flex-wrap","wrap").style("width","100%")
        for i in range(0,int(value)):
            Image(id=f"img{i}",value= f"./image/{i}").on("click", onimageclick)
    connection.send("imagerow", imagerow.render(), "init-content")
 




with Element(id="main") as main:
    main.cls("container").style("width","100%").style("height","100%")
    with Row() as row1:
        row1.cls("container").cls("border").style("width","100%").style("height","100%")
        with Col() as col1:
            col1.cls("w12").cls("border").style("height","50%")
            with Row() as row:
                Label(usefor="a",value="Images:")
                Input(id="a",value="0").on("change", onchangeSlider)
            Slider(id="as",value="0").on("change", onchangeSlider)
        with Col() as col2:
            col2.cls("border").style("height","50%").style("width","100%")
            img = ImageViewer(id="viewer1",value="./image/0")
            img.style("width","100%").style("height","500px")
    with Row() as imagerow:
        imagerow.id = "imagerow"
        imagerow.cls("container").cls("border").style("flex-wrap","wrap").style("width","100%")
        for i in range(0,20):
            with Col() as elm:
                elm.cls("border").cls("p3")
                Image(id=f"img{i}",value= f"./image/{i}").on("click", onimageclick)
                Label(value=f"Image {i}").style("fontSize","12em")
            


def UI():
    return main.render()


