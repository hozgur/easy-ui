from components.element import Element
class Label(Element):
    def __init__(self, usefor = None,value = None):
        super().__init__(value = value)
        self.classes.append("label")
        self.usefor = usefor
        
    def render(self):
        class_str = " ".join(self.classes)
        return f"<label class='{class_str}' for='{self.usefor}'>{self.value}</label>"
    