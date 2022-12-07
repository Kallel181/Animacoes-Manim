from  manim import *
from manim_slides import Slide


class slide0(Slide):
    def construct(self):
        #Apresentação do tema(slide0)
        self.wait()
        self.pause()
        titulo = Tex(r"O coelho e a revolução indrustrial").scale(1.5)
        titulo.shift(UP*2)  
          
        rab = SVGMobject("rabbit.svg")
        rab.next_to(titulo,LEFT)
        rab.shift(DOWN*0.5)
        rab.shift(RIGHT*0.5)
        
        watch = SVGMobject("pocket-watch.svg")
        watch.next_to(titulo,RIGHT)
        watch.shift(DOWN*0.5)
        watch.shift(LEFT*0.5)
        
        watch.scale(0.5)
        rab.scale(0.5)
        
        
        kallel = Tex(r"Kallel Fiori     RA: 770635")
        douglas= Tex(r"Douglas Suzuki   RA: 770615")
        paulo =  Tex(r"Paulo Cezar      RA: 77xxxx")
        
        nomes = VGroup(kallel,douglas,paulo)
        nomes.scale(0.5)
        nomes.move_to(DOWN*2 + LEFT*4)
        nomes.arrange(DOWN,center=False,aligned_edge=LEFT)
        
        
        logo = SVGMobject("dm-logo-vector.svg")
        logo.scale(0.5)
        logo.move_to(DOWN*2 + RIGHT*4)
                
        
        escola_data = Tex(r"Ufscar"+r" - "+r"2022",font_size = 25)
        escola_data.next_to(logo,DOWN)
        logo_data = VGroup(logo,escola_data)
        self.play(Write(rab),Write(titulo),Write(watch),Write(logo_data),Write(nomes))
        
        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()


#image = ImageMobject("Path") use fadein to play 


class slide1(Slide):
    def construct(self):
        pass
