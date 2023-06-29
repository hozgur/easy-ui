from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element, Elm
from components.slider import Slider
from components.button import Button
from components.image import Image
from components.text import Text
from components.script import Script
from components.imageviewer import ImageViewer
import connection

def onclick(id, value):
    print(f"Button {id} clicked")
    Elm("viewer1").value = "./image/0"

def onchange(id, value):
    print(f"Slider Value of {id} changed to {value}")
    a = Elm("a") if id == "as" else Elm("as")
    if a is not None:
        a.value = value
    
with Element(id="main") as main:
    # Button
    Button(id="btn",value="Open Image").on("click", onclick).cls("w12")
    # Col
    with Col() as col:
        col.style("height","50%").style("width","600px")
        #Image
        Image(id="img1",value="./image/0").style("width","auto")
        # Row
        with Row() as row:
            row.cls("container").cls("border")
            # Label
            Label(usefor="a",value="Label:")
            # Input
            Input(id="a",value="0").on("change", onchange)
        # Slider
        Slider(id="as",value="0").on("change", onchange)
        # Text
        Text(id="text",value="Hello World")
        # ImageViewer
        ImageViewer(id="viewer1",value="./image/0")
def UI():
    return main.render()