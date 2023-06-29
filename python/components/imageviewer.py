from components.element import Element
import connection
class ImageViewer(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "div"
        self.id = id
        self.has_content = False
        self.style("width","100%")
        self.style("height","500px")
        self.value_name = None
        if id is not None:
            self.id = id
            connection.queue_for_send(self.id, self.value, "init-seadragon")

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
        src = {
            "type": "image",
            "url": value
        }
        connection.send(self.id, src, "seadragon-open")


        