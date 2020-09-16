"""
03.15: Snømann!

I ezgraphics
"""

# Import ezgraphics
from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()

canvas.drawOval(200,100,100,100)
canvas.drawOval(200,200,100,100)
canvas.drawOval(200,300,100,100)
win.wait()
