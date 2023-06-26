from components.element import Element
class Label(Element):
    def __init__(self,value = None):
        super().__init__(value)
        self.classes.append("label")