"""
03.09: Flere sirkler
"""
import math
from ezgraphics import GraphicsWindow
from ezgraphics import GraphicsCanvas

win = GraphicsWindow(500,500)
window = win.canvas()

for i in range(50):
    window.drawOval(i * 10, math.sin(i) * 40 + 200,20,20)

win.wait()
