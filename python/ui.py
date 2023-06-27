
from components.row import Row
from components.col import Col
from components.input import Input
from components.label import Label
from components.element import Element
from components.slider import Slider

def onchange(elm):
    print("onchange", elm)

with Element() as main:
    main.cls("container").cls("w14").cls("border")
    with Row() as row:
        
        Label(usefor="a",value="A:")
        Input(id="a",value="0").on("change", onchange)
    with Row() as row:
        
        Label(usefor="as",value="A:")
        Slider(id="as",value="0").on("change", onchange)
    with Row() as row:
        
        Label(usefor="b",value="B:")
        Input(id="b",value="0")
    with Row() as row:
        
        Label(usefor="c",value="C:")
        Input(id="c",value="0")

print(main.render())

def UI():
    return main.render()


