from manim_presentation import Slide
from manim import *

class cena0 (Slide):
    def construct(self):
        titulo=Text("CRIANDO ANIMAÇÕES PARA GEOMETRIA ORIENTADAS AO ENSINO \nMÉDIO USANDO A BIBLIOTECA PYTHON MANIM")
        titulo.scale(0.6)
        
        self.play(Write(titulo))
        self.pause()
        
        #-------------------- Objetivos --------------------
        obj_title = Text("Objetivos")
        obj_title.generate_target()
        obj_title.target.scale(0.6)
        obj_title.target.shift(UP*3.5)
        
        self.play(FadeOut(titulo))
        self.play(Write(obj_title))
        self.pause()
        self.play(MoveToTarget(obj_title))
        
        objetivo1=Text("Identêntificar e aplicar os diversos usos da biblioteca Manim em sala de aula")
        objetivo2=Text("Analisar a eficiência do uso das animações geradas pelo Manim em sala de aula")
        objetivo3=Text("Identificar a maneira mais eficiente de se usar animações em sala de aula")
        objetivo1.scale(0.55)
        objetivo2.scale(0.55)
        objetivo3.scale(0.55)
        objetivo1.shift(UP*1.5)
        objetivo2.next_to(objetivo1,DOWN*1.5)
        objetivo3.next_to(objetivo2,DOWN*1.5)              
        
        self.play(Write(objetivo1))
        self.pause()
        self.play(Write(objetivo2))
        self.pause()
        self.play(Write(objetivo3))
        self.pause()
        
        self.play(FadeOut(objetivo1),FadeOut(objetivo2),FadeOut(objetivo3),FadeOut(obj_title))      
        
        #-------------------- Referencial Teórico --------------------
        ref_title = Text("Referencial Teórico")
        ref_title.generate_target()
        ref_title.target.scale(0.6)
        ref_title.target.shift(UP*3.5)
        
        self.play(Write(ref_title))
        self.pause()
        self.play(MoveToTarget(ref_title))
        
        texto1 = Text("Esse projeto de pesquisa possui dois referenciais principais:")
        texto1.scale(0.5)
        texto1.shift(UP)
        
        self.play(Write(texto1))
        self.pause()
        
        ref1 = Text("1) Geogebra: recurso visual e cinestésico no ensino de funções, por:Weddington Galindo Feitoza et. al. ")
        ref2 = Text("2) Manim Community Documentation")
        ref1.scale(0.4)
        ref2.scale(0.4)
        ref1.next_to(texto1,DOWN)
        ref2.next_to(ref1,DOWN)
        
        self.play(Write(ref1))
        self.pause()
        self.play(Write(ref2))
        self.pause()
        self.play(FadeOut(ref1),FadeOut(ref2),FadeOut(texto1),FadeOut(ref_title))
        
        #-------------------- Metodologia da Pesquisa --------------------
        ref_title = Text("Metodologia da Pesquisa")
        ref_title.generate_target()
        ref_title.target.scale(0.6)
        ref_title.target.shift(UP*3.5)
        
        self.play(Write(ref_title))
        self.pause()
        self.play(MoveToTarget(ref_title))
        
        elab_text=Text("Elaboração inicial da\nanimação com o professor")
        elab_icon=SVGMobject("handshake-solid.svg", color = WHITE, stroke_width= 2.0)
        
        elab_icon.scale(0.4)
        elab_text.scale(0.4)
        elab_text.next_to(elab_icon, DOWN)   
        
        elab = Group(elab_text, elab_icon)
        elab.move_to((-5,1.5,0))
        
        self.play(FadeIn(elab))
        self.pause()
                
        anim_text=Text("Construção da animação")
        anim_icon=SVGMobject("laptop-code-solid.svg", color = WHITE, stroke_width= 2.0)
        
        anim_icon.scale(0.4)
        anim_text.scale(0.4)        
        anim_text.next_to(anim_icon, DOWN)        
        
        anim = Group(anim_icon, anim_text)
        anim.next_to(elab, RIGHT*2)
        
        arrow_1 = Arrow(start=elab.get_center(), end=anim.get_center(), color=WHITE, buff = 1, stroke_width=2,max_tip_length_to_length_ratio=0.1)
        self.play(Write(arrow_1))
        self.pause()
        
        self.play(FadeIn(anim))
        self.pause()
        
        
        apre_text=Text("Apresentação da animação")
        apre_icon=SVGMobject("person-chalkboard-solid.svg", color = WHITE, stroke_width= 2.0)
        
        apre_icon.scale(0.4)
        apre_text.scale(0.4)        
        apre_text.next_to(apre_icon, DOWN)        
        
        apre = Group(apre_icon, apre_text)
        apre.next_to(anim, RIGHT*2)
        
        arrow_2 = Arrow(start=anim.get_center(), end=apre.get_center(), color=WHITE, buff = 1, stroke_width=2,max_tip_length_to_length_ratio=0.1)
        self.play(Write(arrow_2))
        self.pause()
        
        self.play(FadeIn(apre))
        self.pause()
        
        
        feed_text=Text("Avaliação dos alunos")
        feed_icon=SVGMobject("file-lines-solid.svg", color = WHITE, stroke_width= 2.0)
        
        feed_icon.scale(0.4)
        feed_text.scale(0.4)        
        feed_text.next_to(feed_icon, DOWN)        
        
        feed = Group(feed_icon, feed_text)
        feed.next_to(apre, RIGHT*2)
        
        arrow_3 = Arrow(start=apre.get_center(), end=feed.get_center(), color=WHITE, buff = 1, stroke_width=2,max_tip_length_to_length_ratio=0.1)
        self.play(Write(arrow_3))
        self.pause()
        
        self.play(FadeIn(feed))
        self.pause()



        relat_text=Text("Relatório final")
        relat_icon=SVGMobject("file-lines-solid.svg", color = WHITE, stroke_width= 2.0)
        
        relat_icon.scale(0.4)
        relat_text.scale(0.4)        
        relat_text.next_to(relat_icon, DOWN)        
        
        relat = Group(relat_icon, relat_text)
        relat.shift(DOWN)
        
        arrow_4 = Arrow(start=elab.get_center(), end=relat.get_center(), color=WHITE, buff = 1.5, stroke_width=2)
        arrow_5 = Arrow(start=anim.get_center(), end=relat.get_center(), color=WHITE, buff = 1, stroke_width=2)
        arrow_6 = Arrow(start=apre.get_center(), end=relat.get_center(), color=WHITE, buff = 1, stroke_width=2)
        arrow_7 = Arrow(start=feed.get_center(), end=relat.get_center(), color=WHITE, buff = 1.5, stroke_width=2)
        
        self.play(Write(arrow_4),Write(arrow_5),Write(arrow_6),Write(arrow_7))
        self.pause()
        self.play(FadeIn(relat))
        self.pause()
        
        
        #exemplo de animação
        
        #cronograma e resultados esperados
        
        
        
        
        
        
        
        self.pause()
        self.wait()