from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512

# Materiales

brick = Material(diffuse = (2.55, 1.27, 0.8), spec = 16,matType = OPAQUE)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8,matType = OPAQUE)

earth = Material(texture = Texture("earthDay.bmp"))
marble = Material(diffuse = (0.8,0.8,0.8), texture = Texture("marble.bmp"), spec = 32, matType= REFLECTIVE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior=1.5, matType = TRANSPARENT)
pinkglass = Material(diffuse = (1.55, 0.92, 1.03), spec = 64, ior=1.5, matType = TRANSPARENT)


rtx = Raytracer(width, height)

# rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
# rtx.lights.append(PointLight((0,5,10), constant = 1.0, linear = 0.1, quad = 0.05, color = (1,1,1)))



rtx.scene.append( Triangle(p1=(2.5,3,-10), p2=(-2.5,3,-10), p3=(0,7,-10),position=(1,1,-10),material=stone))



rtx.glRender()

rtx.glFinish("output.bmp")