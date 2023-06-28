from element import Element
class Image(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.name = "img"
        self.src = None        
    
    def render(self):
        str = f"<{self.name} id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str += f"class='{class_str}'"
        if len(self.styles) > 0:
            str += f"style='{self.styles if self.styles is not None else ''}'"        
        for event_name, action in self.events.items():
            str += f"on{event_name}='clientEmit(this.id,this.value,\"{event_name}\")'"        
        str +=f"src ='{self.value if self.value is not None else ''}'"
        str +=">"
        for child in self.children:
            str += child.render()
        str += f"</{self.name}>"
        return str