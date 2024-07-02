from manim import *

class VisualizeArray(Scene):
    def construct(self):
        array = [1, 2, 3, 4, 5]
        array_mob = VGroup(*[Square().set_fill(BLUE, opacity=1).set_stroke(WHITE) for _ in array])
        array_mob.arrange(RIGHT, buff=0.1)
        
        # Add text for each element
        for i, num in enumerate(array):
            number = Text(str(num)).move_to(array_mob[i])
            array_mob[i].add(number)
        
        self.play(Create(array_mob))
        self.wait()
