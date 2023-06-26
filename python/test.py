import server
from components.row import Row
from components.textbox import TextBox

with Row() as row:
    a = TextBox("a",0)
    a.style("width: 100px; height: 100px; background-color: red;")
    b = TextBox("b",1)
    c = TextBox("c")


server.init = row.render()
print(server.init)

server.start()

