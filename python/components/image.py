from components.element import Element
class Image(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.name = "img"
        self.value_name = "src"
        self.styles.append("width:100px")
        self.classes.append("p3")
        
    def render(self):
        str = f"<{self.name} id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str += f"class='{class_str}'"
        style_str = "; ".join(self.styles)
        if(len(style_str) > 0):
            str += f'style="{style_str}"'      
        for event_name, action in self.events.items():
            str += f"on{event_name}='clientEmit(this.id,this.src,\"{event_name}\")'"        
        str +=f"src ='{self.value if self.value is not None else ''}'"
        str +=">"
        for child in self.children:
            str += child.render()
        str += f"</{self.name}>"
        return str