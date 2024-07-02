from manim import *

class BubbleSort(Scene):
    def construct(self):
        array = [5, 1, 4, 2, 8]
        array_mobs = self.create_array_mobjects(array)
        self.play(*[Write(mob) for mob in array_mobs])

        text = Text("Bubble Sort").to_edge(UP)
        self.play(Write(text))

        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                self.highlight_elements(array_mobs, j, j + 1)
                self.show_arrows(array_mobs, j, j + 1)
                self.wait(1)
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.swap_elements(array_mobs, j, j + 1)
                    self.wait(1)
                self.unhighlight_elements(array_mobs, j, j + 1)
                self.remove_arrows()
        self.wait(2)

    def create_array_mobjects(self, array):
        array_mobs = VGroup(*[self.create_element_mobject(num) for num in array])
        array_mobs.arrange(RIGHT, buff=0)
        return array_mobs

    def create_element_mobject(self, num):
        element = Square(side_length=1)
        num_text = Text(str(num), font_size=36)
        num_text.move_to(element.get_center())
        return VGroup(element, num_text)

    def highlight_elements(self, array_mobs, index1, index2):
        array_mobs[index1][0].set_color(RED)
        array_mobs[index2][0].set_color(RED)

    def unhighlight_elements(self, array_mobs, index1, index2):
        array_mobs[index1][0].set_color(WHITE)
        array_mobs[index2][0].set_color(WHITE)

    def swap_elements(self, array_mobs, index1, index2):
        array_mobs[index1], array_mobs[index2] = array_mobs[index2], array_mobs[index1]
        array_mobs.arrange(RIGHT, buff=0)
        self.play(
            array_mobs[index1].animate.move_to(array_mobs[index1].get_center()),
            array_mobs[index2].animate.move_to(array_mobs[index2].get_center())
        )

    def show_arrows(self, array_mobs, index1, index2):
        self.arrow1 = Arrow(array_mobs[index1].get_bottom(), array_mobs[index1].get_top(), buff=0.1)
        self.arrow2 = Arrow(array_mobs[index2].get_bottom(), array_mobs[index2].get_top(), buff=0.1)
        self.arrow1.shift(DOWN * 1)  # Shift arrow down
        self.arrow2.shift(DOWN * 1)  # Shift arrow down
        self.play(Write(self.arrow1), Write(self.arrow2))

    def remove_arrows(self):
        self.play(FadeOut(self.arrow1), FadeOut(self.arrow2))

