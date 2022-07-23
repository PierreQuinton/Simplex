from manim import *
from typing import Sequence
import numpy as np
import math

class IntroKnownArea(Scene):
  def construct(self):
    # Start with the area of triangle, square, circle
    opa = 0.4     # opacity of figures
    spread = 2.2  # how they spread from center, arranged in triangle
    
    sqr_color = WHITE
    sqr = Square().move_to(spread*UP)
    sqr.set_fill(opacity=opa)
    sqrs = [sqr, Tex('$c$').next_to(sqr,LEFT), Tex('$c$').next_to(sqr,UP)]
    sqr_area = Tex('$c^2$').move_to(sqr.get_center()).set_color(sqr_color)
    sqrs = [a.set_color(sqr_color) for a in sqrs]
    
    circ_scale=1.2
    circ_color = RED
    circ = Circle().scale(circ_scale).move_to((DOWN/2+math.sqrt(3)/2*LEFT)*spread)
    circ.set_fill(opacity=opa)
    ray = Line(circ.get_center(), circ.get_center()+circ_scale*circ.get_radius()*RIGHT)
    circs = [circ, ray, Tex('$r$').next_to(ray,DOWN)]
    circ_area = Tex('$\pi r^2$').next_to(circ.get_center(),UP).set_color(circ_color)
    circs = [a.set_color(circ_color) for a in circs]
    
    tri_scale = 1.5
    tri_color = BLUE
    tri = Triangle().scale(tri_scale).move_to((DOWN/2+math.sqrt(3)/2*RIGHT)*spread)
    tri.set_fill(opacity=opa)
    tri_height = Line(tri.points[0]+DOWN*tri_scale**2,tri.points[0])
    tris = [tri, Tex('$b$').next_to(tri,DOWN),tri_height, Tex('$h$').next_to(tri_height,RIGHT)]
    tri_area = Tex('$\\frac{bh}{2}$').next_to(tri.get_center(),0.8*LEFT+0.15*DOWN).set_color(tri_color)
    tris = [a.set_color(tri_color) for a in tris]
    
    
    
    self.play(FadeIn(*sqrs))
    self.play(FadeIn(sqr_area))
    self.play(FadeIn(*circs))
    self.play(FadeIn(circ_area))
    self.play(FadeIn(*tris))
    self.play(FadeIn(tri_area))
    self.wait()
    self.play(FadeOut(*sqrs,sqr_area,*circs,circ_area,*tris,tri_area))
    

class IntroCutting(Scene):
  def construct(self):
    # start with cutting a figure in two and adding their area
    opa = 0.4
    col = BLUE
    
    points = [
      [-1,2,0],
      [0,2+math.sqrt(3),0],
      [1,2,0],
      [1,0,0],
      [-1,0,0]
    ]
    total = Polygon(*points).set_fill(opacity=opa,color=col)
    sqr = Polygon(points[0],*points[2:]).set_fill(opacity=opa,color=col)
    tri = Polygon(*points[0:3]).set_fill(opacity=opa,color=col)
    pos_tri = tri.get_center()
    pos_sqr = sqr.get_center()
    equal = Tex('$=$').move_to(0.6*DOWN)
    plus = Tex('$+$').move_to(2.5*DOWN)
    self.play(FadeIn(total))
    self.play(FadeIn(sqr,tri))
    self.play(sqr.animate.set_fill(color=RED).move_to(2*RIGHT+2.5*DOWN),
              tri.animate.set_fill(color=GREEN).move_to(2*LEFT+2.5*DOWN),
              FadeIn(equal, plus))
    self.wait(1)

class IntroConclusion(Scene):
  def construct(self):
    self.wait(5)

class Setup(Scene):
  def construct(self):
    func = Tex('$\\lambda:S\\to [0,\\infty[$', font_size=144)
    self.play(FadeIn(func))
    self.wait(1)
    plane_offset=3.5*LEFT
    x_l = 8
    y_l = 7
    plane = Axes(x_range=(-1,x_l-1,1),y_range=(-1,y_l-1,1),x_length=x_l,y_length=y_l).shift(plane_offset)
    self.play(FadeIn(plane), func.animate.scale(1/3).shift(4*RIGHT+2.5*UP))
    def to_plane(o):
      o.move_to(plane.c2p(*o.get_center()))
      return o
    tri_pos = np.array([
      [1,1,0],
      [2,3,0],
      [4,2,0]
    ])
    tri = to_plane(Polygon(*tri_pos,color=YELLOW).set_fill(color=YELLOW,opacity=0.8))
    tri_a = to_plane(Tex('A',font_size=40).next_to(tri_pos[0],0.6*LEFT))
    tri_b = to_plane(Tex('B',font_size=40).next_to(tri_pos[1],0.6*UP))
    tri_c = to_plane(Tex('C',font_size=40).next_to(tri_pos[2],0.6*RIGHT))
    self.play(FadeIn(tri,tri_a,tri_b,tri_c))
    self.wait(2)

