from components.element import Element
class Button(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "button"
        