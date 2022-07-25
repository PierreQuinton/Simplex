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
    sqrs = [sqr, MathTex(r'c').next_to(sqr,LEFT), MathTex(r'c').next_to(sqr,UP)]
    sqr_area = MathTex(r'c^2').move_to(sqr.get_center()).set_color(sqr_color)
    sqrs = [a.set_color(sqr_color) for a in sqrs]
    
    circ_scale=1.2
    circ_color = RED
    circ = Circle().scale(circ_scale).move_to((DOWN/2+math.sqrt(3)/2*LEFT)*spread)
    circ.set_fill(opacity=opa)
    ray = Line(circ.get_center(), circ.get_center()+circ_scale*circ.get_radius()*RIGHT)
    circs = [circ, ray, MathTex(r'r').next_to(ray,DOWN)]
    circ_area = MathTex(r'\pi r^2').next_to(circ.get_center(),UP).set_color(circ_color)
    circs = [a.set_color(circ_color) for a in circs]
    
    tri_scale = 1.5
    tri_color = BLUE
    tri = Triangle().scale(tri_scale).move_to((DOWN/2+math.sqrt(3)/2*RIGHT)*spread)
    tri.set_fill(opacity=opa)
    tri_height = Line(tri.points[0]+DOWN*tri_scale**2,tri.points[0])
    tris = [tri, MathTex(r'b').next_to(tri,DOWN),tri_height, MathTex(r'h').next_to(tri_height,RIGHT)]
    tri_area = MathTex(r'\frac{bh}{2}').next_to(tri.get_center(),0.8*LEFT+0.15*DOWN).set_color(tri_color)
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
    equal = MathTex(r'=').move_to(0.6*DOWN)
    plus = MathTex(r'+').move_to(2.5*DOWN)
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
    func = MathTex(r'\lambda:{{S}}\to [0,\infty[', font_size=144)
    self.play(Write(func))
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
    tri_a = to_plane(MathTex(r'A',font_size=40).next_to(tri_pos[0],0.6*LEFT))
    tri_b = to_plane(MathTex(r'B',font_size=40).next_to(tri_pos[1],0.6*UP))
    tri_c = to_plane(MathTex(r'C',font_size=40).next_to(tri_pos[2],0.6*RIGHT))
    self.play(FadeIn(tri,tri_a,tri_b,tri_c))
    
    
    tri2 = tri.copy()
    tri_eq = MathTex(r'\phantom{x}x', r' = {{\{ t_1 A + t_2 B+ t_3 C : t_1,t_2,t_3\in [0,1], t_1+t_2+t_3=1 \} }}', font_size=35).shift(1.5*UP+RIGHT)
    tri_eq[0].set_color(BLACK).set_fill(opacity=0)
    self.add(tri2)
    self.play(tri2.animate.move_to(tri_eq[0].get_center()).scale(0.1),Write(tri_eq))
    
    tri_in_S_lambda = MathTex(r'{{x}} &\in S\\\lambda({{x}})&\in [0,\infty[').next_to(tri_eq,2*DOWN)
    tri_in_S_lambda[0].set_color(BLACK).set_fill(opacity=0)
    tri_in_S_lambda[2].set_color(BLACK).set_fill(opacity=0)
    tri3 = tri2.copy()
    tri4 = tri2.copy()
    self.play(Write(tri_in_S_lambda))
    self.play(tri3.animate.move_to(tri_in_S_lambda[0].get_center()),
      tri4.animate.move_to(tri_in_S_lambda[2].get_center()))
    
    circ1 = Circle(radius=1.0).move_to(tri.get_center()).set_color(BLUE).set_fill(color=BLUE,opacity=0.8)
    circ_r = Line(circ1.get_center(),circ1.get_center()+RIGHT,color=BLUE)
    circ_O_tex = MathTex(r'O', font_size=30).next_to(circ_r,0.5*LEFT+0.5*UP)
    circ_r_tex = MathTex(r'r', font_size=30).next_to(circ_r,0.5*DOWN)
    circ2 = circ1.copy().scale(0.1).move_to(tri2.get_center())
    circ_eq = MathTex(r'\{ P : \| P-O \|\leq r \}',font_size=35).next_to(tri_eq[1],0.6*RIGHT)
    circ3 = circ2.copy().move_to(tri3.get_center())
    circ4 = circ2.copy().move_to(tri4.get_center())
    
    self.play(Transform(tri,target_mobject=circ1),
      FadeIn(circ_O_tex,circ_r,circ_r_tex),
      Transform(tri2,circ2),Transform(tri_eq[2],circ_eq),
      Transform(tri3,circ3),
      Transform(tri4,circ4),
      FadeOut(tri_a,tri_b,tri_c))
    
    self.wait(2)

