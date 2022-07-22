from manim import *
import math

class SimplexLogo(Scene):
  def construct(self):
    scaling = 1.5
    positions = [
      [0,scaling,0],
      [math.sqrt(3)/2*scaling,-1/2*scaling,0],
      [-math.sqrt(3)/2*scaling,-1/2*scaling,0]
    ]
    points = [Point(p,color=WHITE) for p in positions]
    segs = [Line(p1,p2) for p1,p2 in zip(positions,positions[1:] +[positions[0]])]
    objs = points+segs
    centers = [obj.get_center() for obj in objs]
    self.add(*points,*segs)
    self.play(*[obj.animate.shift(cent) for obj, cent in zip(objs,centers)])
    self.play(*[obj.animate.shift(-4*cent).rotate(math.pi/3) for obj, cent in zip(objs,centers)])
    self.play(*[obj.animate.shift(cent).rotate(2*math.pi/3) for obj, cent in zip(objs,centers)])
    simplex = Text('Simplex',font_size=120).shift(0.5*DOWN)
    self.play(*[obj.animate.shift(5*LEFT) for obj in objs], FadeIn(simplex))
    self.wait(2)
