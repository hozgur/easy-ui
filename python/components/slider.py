from components.element import Element
class Slider(Element):
    def __init__(self,id = None,value = None, min = 0, max = 100, step = 1):
        super().__init__(id = id, value = value)
        self.min = min
        self.max = max
        self.step = step
        
        
    def render(self):
        class_str = " ".join(self.classes)
        str = f"<input type='range' id='{self.id}' class='{class_str}' value='{self.value}'"
        for event_name, action in self.events.items():            
            if event_name == "change":
                str += f"onchange='changeHandler(this.id, this.value)'"
        str += "/>"
        return str
