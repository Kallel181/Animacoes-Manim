from manim import *
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
        paulo =  Tex(r"Paulo Cesar      RA: 770629")
        
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



class slide1(Slide):
    def construct(self):
        #Slide 1        
        #========== String Constants ==========
        TEXT1 = r"Quais elementos estranhos podemos identificar no coelho ?"
        TEXT2 = r"“A personagem Coelho Branco está totalmente ligada à velocidade da Revolução Industrial em sua natureza, por ser um animal de incrível agilidade e astúcia.” (MENDES, 2012)"
        
        
        #======================================
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")  
                
        
        coelho = ImageMobject("Coelho.png")
        coelho.scale(1.3)
        self.play(FadeIn(coelho))
        
        coelho.generate_target().shift(DOWN)
        text1 = Tex(TEXT1, tex_template=myTemplate, tex_environment="justify")
        text1.scale(0.6)
        text1.next_to(coelho.target,UP)
        
        
        self.pause()
        self.play(MoveToTarget(coelho))
        self.wait()
        self.play(Write(text1))
        self.pause()
        
        
        coelho.target.scale(0.8)
        text1.generate_target().shift(UP)
        coelho.target.next_to(text1,DOWN)
        coelho.target.shift(UP)
        
        text2 = Tex(TEXT2, tex_template=myTemplate, tex_environment="justify")   
        text2.scale(0.6)    
        text2.next_to(coelho.target,DOWN)
        
        
        self.play(MoveToTarget(text1))
        self.play(MoveToTarget(coelho))
        self.play(Write(text2))
        
                
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()



class slide2(Slide):
    def construct(self):
        #Slide2               
        #========== String Constants ==========
        HEAD1 = r"Revolução indrustrial"
        TEXT1 = r"$\bullet$Isolamento geográfico"
        TEXT2 = r"$\bullet$Ato de navegação x Rotas marítimas"
        TEXT3 = r"$\bullet$Desenvolvimento náutico"
        TEXT4 = r"$\bullet$Colonialismo"
        TEXT5 = r"$\bullet$Reservas de madeira, carvão e ferro"
        TEXT6 = r"$\bullet$Revolução Gloriosa - Absolutismo x  Monarquia Constitucional Parlamentarist"
        TEXT7 = r"$\bullet$Lei dos cercamentos - Capitalismo x Feudalismo - Êxodo rural"
        TEXT8 = r"$\bullet$Estruturas financeiras - Bolsa de valores de londres e banco da inglaterra"
        TEXT9 = r"$\bullet$Indústria têxtil, máquina a vapor e metalurgia"
        
        IMAGE1_PATH = "mapa.png"

        #======================================
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")    
                
                
        head = Tex(HEAD1,font_size=30)
        head.move_to(UP*3 + LEFT*5)
        self.play(Write(head))
        self.pause()
        
        
        text1 = Tex(TEXT1, tex_template=myTemplate, tex_environment="justify")
        image1 = ImageMobject(IMAGE1_PATH)
        image1.scale(1.5)
        
        
        
        slied_group1 = VGroup(text1)
        slied_group1.scale(0.65)
        slied_group1.move_to(LEFT*3+UP*2)
        
        
        image1.next_to(text1,DOWN)
        image1.shift(RIGHT*2)
        
        slied_group1.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(text1),FadeIn(image1))
        
        self.pause()
        
        self.play(FadeOut(text1),FadeOut(image1))#fade last
        self.pause()
        #====================================PART 2====================================
        
        text2 = Tex(TEXT2, tex_template=myTemplate, tex_environment="justify")
        text3 = Tex(TEXT3, tex_template=myTemplate, tex_environment="justify")
        
        
        slied_group2 = VGroup(text2,text3)
        slied_group2.scale(0.65)
        slied_group2.move_to(LEFT*3+UP*2)
        slied_group2.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(slied_group2))
        
        image2 = ImageMobject("barcos.png")
        image2.scale(1.3)
        image2.next_to(text3,DOWN)
        image2.shift(RIGHT*2)
        self.play(FadeIn(image2))
        self.pause()
        
        
        self.play(FadeOut(slied_group2),FadeOut(image2))#fade last
        self.pause()
        #====================================PART 3====================================
        text4 = Tex(TEXT4, tex_template = myTemplate, tex_environment = "justify")
        text5 = Tex(TEXT5, tex_template = myTemplate, tex_environment = "justify")
        
        
        slied_group3 = VGroup(text4,text5)
        slied_group3.scale(0.65)
        slied_group3.move_to(LEFT*3+UP*2)
        slied_group3.arrange(DOWN,center=False,aligned_edge=LEFT)
        slied_group3.shift(LEFT*2)
        self.play(Write(slied_group3))
        
        image3 = ImageMobject("mapacarvao.png")
        image3.scale(0.9)
        image3.next_to(text3,RIGHT)
        image3.shift(RIGHT*2+DOWN*1.5)
        self.play(FadeIn(image3))
        self.pause()
        
        
        self.play(FadeOut(slied_group3),FadeOut(image3))#fade last
        self.pause()
        #====================================PART 4====================================
        text6 = Tex(TEXT6, tex_template = myTemplate, tex_environment = "justify")
        image4 = ImageMobject("gloriosa.png")
        image4.scale(1.8)
        image4.next_to(text6,DOWN)
        image4.shift(UP*2)
        
        slied_group4 = VGroup(text6)
        slied_group4.scale(0.65)
        slied_group4.move_to(UP*2+RIGHT)
        slied_group4.arrange(DOWN,center=False,aligned_edge=LEFT)
        slied_group4.shift(LEFT*2)
        self.play(Write(slied_group4),FadeIn(image4))
        self.pause()
        
        
        self.play(FadeOut(slied_group4),FadeOut(image4))#fade last
        self.pause()
        #====================================PART 5====================================
        text7 = Tex(TEXT7, tex_template = myTemplate, tex_environment = "justify")
        image5 = ImageMobject("cercamento.png")
        image5.scale(0.7)
        image5.next_to(text7,DOWN)
        image5.shift(UP*2)
        
        slied_group5 = VGroup(text7)
        slied_group5.scale(0.65)
        slied_group5.move_to(UP*2)
        slied_group5.arrange(DOWN,center=False,aligned_edge=LEFT)
        slied_group5.shift(LEFT*2)
        self.play(Write(slied_group5),FadeIn(image5))
        self.pause()
        
        
        self.play(FadeOut(slied_group5),FadeOut(image5))#fade last
        self.pause()
        #====================================PART 6====================================
        text8 = Tex(TEXT8, tex_template = myTemplate, tex_environment = "justify")
        text9 = Tex(TEXT9, tex_template = myTemplate, tex_environment = "justify")
        image6 = ImageMobject("maquina.png")
        image6.scale(0.9)
        image6.next_to(text9,DOWN)
        image6.shift(UP)
        
        slied_group6 = VGroup(text8,text9)
        slied_group6.scale(0.65)
        slied_group6.move_to(UP*2+RIGHT)
        slied_group6.arrange(DOWN,center=False,aligned_edge=LEFT)
        slied_group6.shift(LEFT*2)
        self.play(Write(slied_group6),FadeIn(image6))

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()

class slidex(Slide):
    def construct(self):
        #Slide2               
        #========== String Constants ==========
        HEAD1 = r"Referências"

        #======================================
        head = Tex(HEAD1,font_size=30)
        head.move_to(UP*3 + LEFT*5)
        self.play(Write(head))     
        
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")    
                
                
        ref1 = Tex(r"[1] MENDES, Mirian Regina. $\textbf{SEGUINDO O COELHO BRANCO: LEWIS CARROLL E A REVOLUCAO INDUSTRIAL INGLESA}$[s. l.], Disponível em: https://www.academia.edu/6940825/SEGUINDO\_O\_COELHO\_BRANCO\_LEWIS\_CARROLL\_E\_A\_REVOLU\_INDUSTRIAL\_INGLESA. Acesso em: 5 dez. 2022.", tex_template=myTemplate, tex_environment="justify")
        ref2 = Tex(r"[2] INDUSTRIAL HISTORY OF EUROPEAN COUNTRIES.$\textbf{United Kingdom-ERIH.}$ [S.l.],2019.Disponível em: https://www.erih.net/how-it-started/industrial-history-of-european-countries/united-kingdom. Acesso em: 10 dez. 2022.‌", tex_template=myTemplate, tex_environment="justify")
        
        referencias = VGroup(ref1,ref2).arrange(DOWN,center=False,aligned_edge=LEFT,buff=1.5)
        referencias.scale(0.4)
        referencias.shift(UP*3)
        
        self.play(Write(referencias))
        
        
        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
