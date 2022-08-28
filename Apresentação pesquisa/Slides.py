from manim_presentation import Slide
from manim import *

class cena0(Slide):
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
        
        self.play(FadeOut(arrow_1),FadeOut(arrow_2),FadeOut(arrow_3),FadeOut(arrow_4),FadeOut(arrow_5),FadeOut(arrow_6),FadeOut(arrow_7),FadeOut(relat),FadeOut(feed),FadeOut(apre),FadeOut(anim),FadeOut(elab),FadeOut(ref_title))  
        
        self.pause()

        #-------------------- Exemplo de animação --------------------
        pit = Text("Exemplo de animação")
        pit.generate_target()
        pit.target.scale(0.6)
        pit.target.shift(UP*3.5)
        self.bring_to_front(pit)
        
        self.play(Write(pit))
        self.pause()
        self.play(MoveToTarget(pit))
        #Modified from https://github.com/H2O-YT/videos-en/blob/main/2021/pythagoras/pythagoras.py    
        
        tri1 = Polygon([-1.5, 1.0, 0.0], [-1.5, -1.0, 0.0], [1.5, -1.0, 0.0]).set_fill(color=BLUE_E, opacity=1.0)
        tri2 = Polygon([1.5, -1.0, 0.0], [3.5, -1.0, 0.0], [3.5, 2.0, 0.0]).set_fill(color=BLUE_E, opacity=1.0)
        tri3 = Polygon([3.5, 2.0, 0.0], [3.5, 4.0, 0.0], [0.5, 4.0, 0.0]).set_fill(color=BLUE_E, opacity=1.0)
        tri4 = Polygon([0.5, 4.0, 0.0], [-1.5, 4.0, 0.0], [-1.5, 1.0, 0.0]).set_fill(color=BLUE_E, opacity=1.0)
        sq = Polygon([-1.5, 1.0, 0.0], [1.5, -1.0, 0.0], [3.5, 2.0, 0.0], [0.5, 4.0, 0.0], color=GREEN).set_fill(color=GREEN_E, opacity=1.0)
        group = VGroup(tri1, tri2, tri3, tri4, sq).scale(0.75)
        tex1 = MathTex("a", color=YELLOW).next_to(tri1.get_bottom(), DOWN)
        tex2 = MathTex("b", color=YELLOW).next_to(tri1.get_left(), LEFT)
        tex3 = MathTex("c", color=YELLOW).next_to(Line(tri1.get_vertices()[0], tri1.get_vertices()[2]), UP, buff=-0.5)
        texg = VGroup(tex1, tex2, tex3)
        tex4 = MathTex("a", color=YELLOW).next_to(tri2.get_right(), RIGHT)
        tex5 = MathTex("b", color=YELLOW).next_to(tri2.get_bottom(), DOWN)
        tex6 = MathTex("c", color=YELLOW).next_to(Line(tri2.get_vertices()[0], tri2.get_vertices()[2]), LEFT, buff=-0.5)
        texg2 = VGroup(tex4, tex5, tex6)
        tex7 = MathTex("a", color=YELLOW).next_to(tri3.get_top(), UP)
        tex8 = MathTex("b", color=YELLOW).next_to(tri3.get_right(), RIGHT)
        tex9 = MathTex("c", color=YELLOW).next_to(Line(tri3.get_vertices()[0], tri3.get_vertices()[2]), DOWN, buff=-0.5)
        texg3 = VGroup(tex7, tex8, tex9)
        tex10 = MathTex("a", color=YELLOW).next_to(tri4.get_left(), LEFT)
        tex11 = MathTex("b", color=YELLOW).next_to(tri4.get_top(), UP)
        tex12 = MathTex("c", color=YELLOW).next_to(Line(tri4.get_vertices()[0], tri4.get_vertices()[2]), RIGHT, buff=-0.5)
        texg4 = VGroup(tex10, tex11, tex12)
        group_full = VGroup(group, texg, texg2, texg3, texg4).next_to(pit, DOWN)
        group_full.shift(LEFT*3)
        self.play(DrawBorderThenFill(tri1))
        self.play(Write(texg))
        self.pause()
        tri1c = tri1.copy()
        self.play(Rotate(tri1c, PI/2, about_point=tri1c.get_vertices()[2]))
        self.play(TransformMatchingShapes(tri1c, tri2))
        tri2c = tri2.copy()
        self.play(Rotate(tri2c, PI/2, about_point=tri2c.get_vertices()[2]))
        self.play(TransformMatchingShapes(tri2c, tri3))
        tri3c = tri3.copy()
        self.play(Rotate(tri3c, PI/2, about_point=tri3c.get_vertices()[2]))
        self.play(TransformMatchingShapes(tri3c, tri4))

        self.play(Write(texg2))

        self.play(Write(texg3))

        self.play(Write(texg4))

        self.bring_to_back(sq)
        self.play(FadeIn(sq))
        self.pause()
        
        expression = MathTex("A_{\\mathrm{ab}}=A_{\\mathrm{c}}+4A_{\\mathrm{tri}}").next_to(group_full, RIGHT*3)
        expression.shift(UP)
        expression.shift(RIGHT)
        self.play(Write(expression))
        self.play(Indicate(tex1, color=WHITE))
        self.play(Indicate(tex5, color=WHITE))
        self.pause()
        expression2 = MathTex("(", "a\\relax", "+", "b\\relax", ")^2", "=", "c\\relax", "^2+4A_{\\mathrm{tri}}").set_color_by_tex("a\\relax", YELLOW).set_color_by_tex("b\\relax", YELLOW).set_color_by_tex("c\\relax", YELLOW).next_to(expression, DOWN)
        group1 = VGroup()
        for i in range(5):
            group1.add(expression2[i])
        self.play(Write(group1))
        self.pause()
        group2 = VGroup()
        for i in range(5, 8):
            group2.add(expression2[i])
        self.play(Write(group2))
        self.pause()
        self.play(FadeOut(expression), expression2.animate.next_to(expression, DOWN))
        self.pause()
        self.play(Indicate(tex1, color=WHITE))
        self.play(Indicate(tex2, color=WHITE))
        self.pause()
        expression3 = MathTex("(", "a\\relax", "+", "b\\relax", ")^2=", "c\\relax", "^2+4", "{a\\relax", "b\\relax", "\\over 2}").set_color_by_tex("a\\relax", YELLOW).set_color_by_tex("b\\relax", YELLOW).set_color_by_tex("c\\relax", YELLOW).next_to(expression2, DOWN)
        self.play(Write(expression3))
        self.pause()
        self.play(FadeOut(expression2), expression3.animate.next_to(expression, DOWN))
        self.pause()
        expression4 = MathTex("a\\relax", "^2", "+", "2", "a\\relax", "b\\relax", "+", "b\\relax", "^2", "=", "c\\relax", "^2", "+", "2", "a\\relax", "b\\relax").set_color_by_tex("a\\relax", YELLOW).set_color_by_tex("b\\relax", YELLOW).set_color_by_tex("c\\relax", YELLOW).next_to(expression3, DOWN)
        for i in range(9):
            self.add(expression4[i])
            self.wait(0.25)
        self.pause()
        for i in range(9, len(expression4)):
            self.add(expression4[i])
            self.wait(0.1)
        self.pause()
        self.play(FadeOut(expression3), expression4.animate.next_to(expression, DOWN))
        self.pause()
        g = VGroup()
        for i in range(2, 6):
            g.add(expression4[i])
        cr1 = Cross(g, color=RED)[0]
        g2 = VGroup()
        for i in range(12, 16):
            g2.add(expression4[i])
        cr2 = Cross(g2, color=RED)[0]
        self.play(Create(cr1), Create(cr2))
        self.pause()
        expression5 = MathTex("a\\relax", "^2", "+", "b\\relax", "^2", "=", "c\\relax", "^2").set_color_by_tex("a\\relax", YELLOW).set_color_by_tex("b\\relax", YELLOW).set_color_by_tex("c\\relax", YELLOW).next_to(expression4, DOWN)
        for i in expression5:
            self.add(i)
            self.wait(0.1)
        self.pause()
        self.play(FadeOut(expression4), FadeOut(cr1), FadeOut(cr2), expression5.animate.next_to(expression, DOWN))
        self.play(Circumscribe(expression5))
        self.pause()       
        self.play(*[FadeOut(mob)for mob in self.mobjects])  
        #-------------------- Cronograma --------------------
        crono_title = Text("Cronograma")
        crono_title.generate_target()
        crono_title.target.scale(0.6)
        crono_title.target.shift(UP*3.5)
        
        self.play(Write(crono_title))
        self.pause()
        self.play(MoveToTarget(crono_title))
        
        atv = Text("Atividades")

        mes_jan = Text("Jan")
        mes_jan.next_to(atv,RIGHT,buff=1)
        
        mes_fev = Text("Fev")
        mes_fev.next_to(mes_jan,RIGHT,buff=1)
        
        mes_mar = Text("Mar")
        mes_mar.next_to(mes_fev,RIGHT,buff=1)
        
        mes_abr = Text("Abr")
        mes_abr.next_to(mes_mar,RIGHT,buff=1)
        
        mes_mai = Text("Mai")
        mes_mai.next_to(mes_abr,RIGHT,buff=1)
        
        mes_jun = Text("Jun")
        mes_jun.next_to(mes_mai,RIGHT,buff=1)
        
        mes_jul = Text("Jul")
        mes_jul.next_to(mes_jun,RIGHT,buff=1)
        
        mes_ago = Text("Ago")
        mes_ago.next_to(mes_jul,RIGHT,buff=1)
        
        mes_set = Text("Set")
        mes_set.next_to(mes_ago,RIGHT,buff=1)
        
        mes_out = Text("Out")
        mes_out.next_to(mes_set,RIGHT,buff=1)
        
        mes_nov = Text("Nov")
        mes_nov.next_to(mes_out,RIGHT,buff=1)
        
        mes_dez = Text("Dez")
        mes_dez.next_to(mes_nov,RIGHT,buff=1)
        
        
        
        elab = Text("Elaboração\ndo projeto")
        elab.next_to(atv,DOWN,buff=1)
        
        rev = Text("Revisão\nbibiliografia")
        rev.next_to(elab,DOWN,buff=1)
        
        ela_anim = Text("Elaboração\ndas animações")
        ela_anim.next_to(rev,DOWN,buff=1)
        
        col = Text("Coleta de\ndados")
        col.next_to(ela_anim,DOWN,buff=1)
        
        relat = Text("Elaboração\nde relatórios")
        relat.next_to(col,DOWN,buff=1)
        
        apre = Text("Apresentação\nde relatórios")
        apre.next_to(relat,DOWN,buff=1)

        crono = VGroup(atv,apre,mes_jan,mes_fev,mes_mar,mes_abr,mes_mai,mes_jun,mes_jul,mes_ago,mes_set,mes_out,mes_nov,mes_dez,elab,rev,ela_anim,col,relat)
        crono.scale(0.4)
        crono.move_to((0,0,0))
        
        self.play(Write(crono))
        self.pause()

        
        def center_position(obj1,obj2):
            return (obj2.get_center()[0],obj1.get_center()[1],0)
        
        check1=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check1.scale(0.1)
        check1.move_to(center_position(elab,mes_jan))
        
        check2=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check2.scale(0.1)
        check2.move_to(center_position(elab,mes_fev))
        
        
        
        check3=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check3.scale(0.1)
        check3.move_to(center_position(rev,mes_fev))
        
        check4=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check4.scale(0.1)
        check4.move_to(center_position(rev,mes_mar))
        
        check5=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check5.scale(0.1)
        check5.move_to(center_position(rev,mes_abr))
        
        check6=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check6.scale(0.1)
        check6.move_to(center_position(rev,mes_mai))
        
        check7=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check7.scale(0.1)
        check7.move_to(center_position(rev,mes_jun))
        
        
        check8=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check8.scale(0.1)
        check8.move_to(center_position(ela_anim,mes_mar))
        
        check9=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check9.scale(0.1)
        check9.move_to(center_position(ela_anim,mes_abr))
        
        check10=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check10.scale(0.1)
        check10.move_to(center_position(ela_anim,mes_mai))
        
        check11=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check11.scale(0.1)
        check11.move_to(center_position(ela_anim,mes_jun))
        
        check12=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check12.scale(0.1)
        check12.move_to(center_position(ela_anim,mes_jul))
        
        check13=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check13.scale(0.1)
        check13.move_to(center_position(ela_anim,mes_ago))
        
        check14=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check14.scale(0.1)
        check14.move_to(center_position(ela_anim,mes_set))
        
        
        
        check15=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check15.scale(0.1)
        check15.move_to(center_position(col,mes_mar))
        
        check16=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check16.scale(0.1)
        check16.move_to(center_position(col,mes_abr))
        
        check17=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check17.scale(0.1)
        check17.move_to(center_position(col,mes_mai))
        
        check18=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check18.scale(0.1)
        check18.move_to(center_position(col,mes_jun))
        
        check19=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check19.scale(0.1)
        check19.move_to(center_position(col,mes_jul))
        
        check20=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check20.scale(0.1)
        check20.move_to(center_position(col,mes_ago))
        
        check21=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check21.scale(0.1)
        check21.move_to(center_position(col,mes_set))
        
        
        
        check22=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check22.scale(0.1)
        check22.move_to(center_position(relat,mes_abr))
        
        check23=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check23.scale(0.1)
        check23.move_to(center_position(relat,mes_jun))
        
        check24=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check24.scale(0.1)
        check24.move_to(center_position(relat,mes_ago))
        
        check25=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check25.scale(0.1)
        check25.move_to(center_position(relat,mes_set))
        
        check26=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check26.scale(0.1)
        check26.move_to(center_position(relat,mes_out))
        
        
        
        check27=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check27.scale(0.1)
        check27.move_to(center_position(apre,mes_nov))
        
        check28=SVGMobject("check-solid.svg", color = WHITE, stroke_width= 2.0)
        check28.scale(0.1)
        check28.move_to(center_position(apre,mes_dez))
        
        
        
        checks = VGroup(check1,check2,check3,check4,check5,check6,check7,check8,check9,check10,check11,check12,check13,check14,check15,check16,check17,check18,check19,check20,check21,check22,check23,check24,check25,check26,check27,check28)
        
        self.play(Create(checks))
        self.pause()
        
        
        self.play(*[FadeOut(mob)for mob in self.mobjects])        
        
        #-------------------- Resultados esperados --------------------
        res_title = Text("Resultados esperados")
        res_title.generate_target()
        res_title.target.scale(0.6)
        res_title.target.shift(UP*3.5)
        
        self.play(Write(res_title))
        self.pause()
        self.play(MoveToTarget(res_title))
        
        res1 = Text("Com o uso das animações esperamos ter uma visivel melhora no desempenho dos alunos\n dentro dos conteudos da geometria")
        res1.scale(0.5)
        res1.shift(UP)
        self.play(Write(res1))
        
        res2 = Text("Tambem esperamos conseguir analisar se há uma forma ideal de organizar as animações\n e apresentá-las em sala de aula")
        res2.scale(0.5)
        res2.next_to(res1,DOWN)
        self.play(Write(res2))     
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])  
        self.pause()
        self.wait()
