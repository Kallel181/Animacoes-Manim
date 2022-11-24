from manim import *
from manim_slides import Slide


#============== Constants ==============
TITULO = "Semelhança de triângulos"
AUTOR = "Kallel Fiori"
NOME_DA_ESCOLA = "Ufscar"
DATA = "2022"
LOGO = "dm-logo-vector.svg"
have_logo = True
MUNICIPIO ="São Carlos/SP"
COMP_CURRICULAR = "Matemática"
NIVEL_ESCOLAR = "9º Ano"
PROFESSOR_RESPONSAVEL = "Kallel Vinicius Rocha Fiori"
UNIDADE_DIDATICA = ""
BASES_LEGAIS = "Ciências da natureza e Matemática"
HABILIDADE_BNCC = ""
OBJETIVOS = ""
#=======================================


class slide0(Slide):
    def construct(self):
        #Slide de apresentação 
        plano = Text("Plano de aula", font_size = 80)
        plano.shift(UP*2)        
                
        
        tema = Text(TITULO,font_size= 30)
        tema.next_to(plano,DOWN*2)        
        plano_tema = VGroup(plano,tema)
        self.play(Write(plano_tema))


        autor = Text("Criado por: "+AUTOR,font_size=20)
        autor.move_to(DOWN*3 + LEFT*4)
        self.play(Write(autor))
                
        
        logo = SVGMobject(LOGO)
        logo.scale(0.5)
        logo.move_to(DOWN*2 + RIGHT*4)
                
        
        escola_data = Text(NOME_DA_ESCOLA+" "+DATA,font_size = 25)
        escola_data.next_to(logo,DOWN)
        logo_data = VGroup(logo,escola_data)
        self.play(Write(logo_data))
        
        

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()



class slide1(Slide):
    def construct(self):
        plano = Text ("Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        nome_escola = Text("-Nome da escola: "+NOME_DA_ESCOLA)
        municipio = Text("-Município da escola: "+MUNICIPIO)
        municipio.next_to(nome_escola,DOWN)
        comp_curricular = Text("-Componente curricular: "+COMP_CURRICULAR)
        comp_curricular.next_to(municipio,DOWN)
        nivel_escolar = Text("-Nível escolar: "+NIVEL_ESCOLAR)
        nivel_escolar.next_to(comp_curricular,DOWN)
        professor_responsavel = Text("-Professor responsável: "+PROFESSOR_RESPONSAVEL)
        professor_responsavel.next_to(nivel_escolar,DOWN)
        
        
        slied1_group = VGroup(nome_escola,municipio,comp_curricular,nivel_escolar,professor_responsavel)
        slied1_group.scale(0.65)
        slied1_group.move_to(LEFT*3+UP*1)
        slied1_group.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(slied1_group))

        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()



class slide2(Slide):
    def construct(self):
        plano = Text ("Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        unidade_didatica = Text("-Unidade Didática: "+UNIDADE_DIDATICA)
        bases_legais = Text("-Bases legais: "+BASES_LEGAIS)
        bases_legais.next_to(unidade_didatica,DOWN)
        
        
        
        slied1_group = VGroup()
        slied1_group.scale(0.65)
        slied1_group.move_to(LEFT*3+UP*1)
        slied1_group.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(slied1_group))

        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()