
from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element, Elm
from components.slider import Slider

def onchange(id, value):
    print(f"Value of {id} changed to {value}")

def onchangeSlider(id, value):
    print(f"Slider Value of {id} changed to {value}")
    a = Elm("a")
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
        


with Element() as main:
    main.cls("container").cls("w14").cls("border")
    with Row() as row:
        
        Label(usefor="a",value="A:")
        Input(id="a",value="0").on("change", onchange)
    with Row() as row:
        
        Label(usefor="as",value="A:")
        Slider(id="as",value="0").on("change", onchangeSlider)
    with Row() as row:
        
        Label(usefor="b",value="B:")
        Input(id="b",value="0")
    with Row() as row:
        
        Label(usefor="c",value="C:")
        Input(id="c",value="0")

def UI():
    return main.render()


