from manim import *
class xd123(Scene):
    def construct(self):
       rect1 =  Rectangle(height=0.5 , width=0.5, fill_opacity = 1).shift(LEFT*5)
       rect2 =  Rectangle(height=0.5 , width=0.5, fill_opacity = 1)
       self.play(Write(rect1))
       self.play(Write(rect2))
       c= NumberPlane().add_coordinates()    
       self.play(Write(c))

       self.wait(3)

