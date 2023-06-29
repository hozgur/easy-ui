
import connection
root = None
cur_parent = None
old_parent = None
elements = {}
created = False
def clientHandler(id, value,event_name):
    global elements
    if id == "myapp":
        if value == "init":
            created = True
            print("Client connected")
    else:
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
        self.styles = []
        self.classes = []
        self.parent = None
        self.value_name = "value"
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
        connection.send(self.id, value, "change-"+self.value_name)

    def add_child(self, child):        
        self.children.append(child)

    def __enter__(self):        
        global cur_parent
        cur_parent = self
        self.children = []
        return self
    
    def __exit__(self, type, value, traceback):        
        global cur_parent
        cur_parent = self.parent
        
    def __str__(self):
        return self.render()
    
    def cls(self,class_name):
        self.classes.append(class_name)
        return self

    def style(self,style):
        self.styles.append(style)
        return self
    
    def on(self,event_name,action):
        self.events[event_name] = action
        return self
    
    
    def render(self):
        str = f"<{self.name} id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str += f"class='{class_str}'"
        style_str = "; ".join(self.styles)
        if(len(style_str) > 0):
            str += f'style="{style_str}"'
        for event_name, action in self.events.items():
            str += f"on{event_name}='clientEmit(this.id,this.value,\"{event_name}\")'"
        str +=">"
        str +=f"{self.value if self.value is not None else ''}"
        for child in self.children:
            str += child.render()
        str += f"</{self.name}>"
        return str
