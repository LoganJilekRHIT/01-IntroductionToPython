"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Logan Jilek.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
hi = rg.SimpleTurtle('turtle')
hi.pen = rg.Pen('cyan',40)
hi.speed = 20
hi.pen_up()
hi.go_to(rg.Point(-200,-300))
hi.pen_down()
hi.left(90)
hi.forward(600)
hi.pen_up()
hi.backward(300)
hi.right(90)
hi.pen_down()
hi.forward(100)
hi.pen_up()
hi.go_to(rg.Point(-100, 300))
hi.pen_down()
hi.right(90)
hi.forward(600)
hi.left(180)
hi.pen_up()
hi.go_to(rg.Point(0, -300))
hi.pen_down()
hi.forward(200)
hi.pen_up()
hi.forward(200)
hi.pen_down()
hi.forward(10)


circle = rg.SimpleTurtle('triangle')
circle.speed = 10
circle.pen = rg.Pen('red',10)
circle.left(90)
circle.pen_up()
circle.go_to(rg.Point(300,200))
size = 100
for k in range(5):
    circle.pen_down()
    circle.draw_circle(size)
    circle.pen_up()
    circle.left(90)
    circle.forward(20)
    circle.right(90)
    circle.pen_down()
    size = size - 20






window.close_on_mouse_click()
