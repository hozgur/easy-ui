from components.element import Element
import connection
class Script(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
    
    def render(self):
        connection.send(self.id, self.value, "script")
        return ""

        
        