
root = None
cur_parent = None
old_parent = None
functions = []
class Element:
    def __init__(self,id = None,value = None):
        global root, cur_parent
        self.name = "div"
        self.id = id
        self.value = value
        self.children = []
        self.events = {}
        self.styles = None
        self.classes = []
        self.parent = None
        print("Creating element: ", self.name, self.value)

        if root is None:
            root = self
            cur_parent = self
            self.parent = None
        else:
            if cur_parent is not None:
                self.parent = cur_parent
                cur_parent.add_child(self)
            else:
                self.parent = None
                cur_parent = self

    def add_child(self, child):
        print("Adding child: ", child.name, child.value)
        self.children.append(child)

    def __enter__(self):
        print("Entering: ", self.name, self.value)
        global cur_parent, old_parent
        old_parent = cur_parent
        cur_parent = self
        return self
    
    def __exit__(self, type, value, traceback):
        print("Exiting: ", self.name, self.value)
        global cur_parent, old_parent
        cur_parent = old_parent
        old_parent = None
        
    def __str__(self):
        return self.render()
    def cls(self,class_name):
        self.classes.append(class_name)
        return self

    def style(self,style):
        self.styles = style
        return self    
    def on(self,event_name,action):
        self.events[event_name] = action
        return self
    def render(self):
        class_str = " ".join(self.classes)
        str = f"<{self.name} class='{class_str}'"
        str += f"style='{self.styles if self.styles is not None else ''}'"        
        for event_name, action in self.events.items():            
            if event_name == "change":
                str += f"onchange='changeHandler(this.value)'"
        str +=">"
        str +=f"{self.value if self.value is not None else ''}"
        for child in self.children:
            str += child.render()
        str += f"</{self.name}>"
        return str
