
from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element, Elm
from components.slider import Slider
from components.button import Button
from components.image import Image
import connection
def onclick(id, value):
    print(f"Button {id} clicked")
    with Row(id="rowB") as row:
        Label(usefor="b",value="B:")
        Input(id="b",value="0")
        Slider(id="bs",value="0").on("change", onchangeSlider)
    connection.send("rowB", row.render(), "init-content")
 

def onchange(id, value):
    print(f"Value of {id} changed to {value}")

def onchangeSlider(id, value):
    print(f"Slider Value of {id} changed to {value}")
    a = Elm(id[:1])
    if a is not None:
        a.value = value
    calc()

def calc():
    a = Elm("a")
    b = Elm("b")
    c = Elm("c")
    if a is not None and b is not None and c is not None:
        vala = float(a.value)
        valb = float(b.value)
        valc = vala + valb
        c.value = str(valc)
        

with Element(id="main") as main:
    main.cls("container").style("width:100%").style("height:100%")
    with Row() as row1:
        row1.cls("container").cls("border")
        with Col() as col1:
            col1.cls("w12").cls("border")
            with Row() as row: 
                Label(usefor="a",value="A:")
                Input(id="a",value="0").on("change", onchange)
            with Row() as row:
                Label(usefor="as",value="A:")
                Slider(id="as",value="0").on("change", onchangeSlider)
            with Row() as row:
                row.id = "rowB"
                Label(usefor="b",value="B:")
                Input(id="b",value="0")
            with Row() as row:        
                Label(usefor="c",value="C:")
                Input(id="c",value="0")



