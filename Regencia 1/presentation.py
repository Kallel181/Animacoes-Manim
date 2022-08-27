from manim import *
from manim_presentation import Slide

class cena0(Slide):
    def construct(self):
        axes = Axes(
            x_range=[-2, 16.3, 1],
            y_range=[-2, 12.03, 1],
            x_length=18,
            y_length=14,            
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-2, 16.01, 1)
            },
            y_axis_config={
                "numbers_to_include": np.arange(-2, 12.01, 1)
            },
            tips=False,
        )
        
        axes.scale(0.5)
        
        #----------Axes----------      
        self.play(Write(axes))
        self.pause()
               
        #----------Graficos----------
        graph1 = axes.plot(lambda x: x -5, x_range=[-2, 16], use_smoothing=True, color=BLUE)
        graph2 = axes.plot(lambda x: x *2 -20, x_range=[-2, 16], use_smoothing=True, color=GREEN)
        self.play(Write(graph1))
        self.pause()
        self.play(Write(graph2))
        self.pause()
        
        #----------Inter----------
        dot = Dot(point=axes.c2p(15,10,0), color=WHITE)
        self.play(Write(dot))
        self.pause()
        
        #----------Inter Lines----------
        line1 = axes.get_vertical_line(axes.input_to_graph_point(15,graph1), color= YELLOW)
        line2 = axes.get_horizontal_line(axes.input_to_graph_point(15,graph1), color= YELLOW)
        self.play(Write(line1))
        self.pause() 
        self.play(Write(line2))
        self.pause()
        
        #----------coords----------
        text = Text("(15,10)")
        text.next_to(dot, direction=RIGHT)
        text.scale(0.6)
        self.play(Write(text))
        self.pause()   
        self.wait()