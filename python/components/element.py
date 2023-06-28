
import connection
root = None
cur_parent = None
old_parent = None
elements = {}

def clientHandler(id, value,event_name):
    global elements
    if id in elements:
        elm = elements[id]
        if elm is not None:            
            if event_name in elm.events:
                elm.events[event_name](id, value)

connection.clientHandler = clientHandler

def Elm(id):
    global elements
    if id in elements:
        return elements[id]
    else:
        return None

class Element:
    def __init__(self,id = None,value = None):
        global root, cur_parent
        self.name = "div"
        self.id = id
        self._value = value
        self.children = []
        self.events = {}
        self.styles = None
        self.classes = []
        self.parent = None
        if id is not None:
            elements[id] = self

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
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
        connection.send(self.id, value)

    def add_child(self, child):        
        self.children.append(child)

    def __enter__(self):        
        global cur_parent, old_parent
        old_parent = cur_parent
        cur_parent = self
        return self
    
    def __exit__(self, type, value, traceback):        
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
            str += f"on{event_name}='clientEmit(this.id,this.value,\"{event_name}\")'"
        str +=">"
        str +=f"{self.value if self.value is not None else ''}"
        for child in self.children:
            str += child.render()
        str += f"</{self.name}>"
        return str
