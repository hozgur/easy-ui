from components.element import Element
class Input(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)                
        
    def render(self):
        class_str = " ".join(self.classes)
        return f"<input type='text' id='{self.id}' class='{class_str}' value='{self.value}'/>"
        