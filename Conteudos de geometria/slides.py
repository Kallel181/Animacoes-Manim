from manim import *
from manim_slides import Slide


#============== Strings Constants ==============

TITULO = r"Semelhança de triângulos"
AUTOR = r"Criado por: Kallel Fiori"
NOME_DA_ESCOLA = r"Ufscar"
DATA = r"2022"
LOGO = "dm-logo-vector.svg"
have_logo = True

MUNICIPIO = r"$\bullet$Município: São Carlos/SP"
COMP_CURRICULAR = r"$\bullet$Componente curricular: Matemática"
NIVEL_ESCOLAR = r"$\bullet$Nível escolar: $9^o$ Ano"
PROFESSOR_RESPONSAVEL = r"$\bullet$Professor responsável: Kallel Vinicius Rocha Fiori"

UNIDADE_DIDATICA = r"$\bullet$Unidade Didática: Semelhança de triângulos e seus casos."
BASES_LEGAIS = r"$\bullet$Bases legais: Ciências da natureza e Matemática"
HABILIDADE_BNCC = r"$\bullet$Habilidade(s) da BNCC: ($\textbf{EF09MA12}$) Reconhecer as condições necessárias e suficientes para que dois triângulos sejam semelhantes.}"

OBJETIVOS = r"$\bullet$Objetivos: Identificar semelhanças entre triângulos, interpretar e analisar as condições de semelhanças e aplicar as regras de semelhanças em exemplos da aula e exercícios."

RECURSOS_DIDATICOS = r"$\bullet$Recursos didáticos: lousa, giz e régua para o professor. Para os alunos, caderno, caneta(ou lápis) e régua."
METODOLOGIA = r"$\bullet$Metodologia: Aula expositiva em primeiro momento. Em um segundo momento, atividades de identificação das semelhanças de forma participativa."
TEMPO_PREVISTO = r"$\bullet$Tempo previsto: XX minutos."
CONTEUDO_CURRICULAR = r"$\bullet$Conteúdo curricular: Semelhança de triângulos."
PRE_REQUISITOS_CURRICULARES = r"$\bullet$Pré-requisitos curriculares dos alunos: ângulos e medidas."
AVALIACAO = r"$\bullet$Avaliação do aprendizado: A avaliação será composta da participação em aula e da lista de exercícios resolvida."

#==================================================


class slide0(Slide):
    def construct(self):
        #Slide de apresentação 
        plano = Tex(r"Plano de aula", font_size = 80)
        plano.shift(UP*2)        
                
        
        tema = Tex(TITULO,font_size= 30)
        tema.next_to(plano,DOWN*2)        
        plano_tema = VGroup(plano,tema)
        self.play(Write(plano_tema))


        autor = Tex(AUTOR,font_size=20)
        autor.move_to(DOWN*3 + LEFT*4)
        self.play(Write(autor))
                
                
        logo = SVGMobject(LOGO)
        logo.scale(0.5)
        logo.move_to(DOWN*2 + RIGHT*4)
                
        
        escola_data = Tex(NOME_DA_ESCOLA+r" "+DATA,font_size = 25)
        escola_data.next_to(logo,DOWN)
        logo_data = VGroup(logo,escola_data)
        self.play(Write(logo_data))
        
        

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()



class slide1(Slide):
    def construct(self):
        #Nome da escola/Municipio/componente curricular/nivel escolar/professor responsavel
        plano = Tex (r"Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        nome_escola = Tex(r"$\bullet$Nome da escola: "+NOME_DA_ESCOLA)
        municipio = Tex(MUNICIPIO)
        municipio.next_to(nome_escola,DOWN)
        comp_curricular = Tex(COMP_CURRICULAR)
        comp_curricular.next_to(municipio,DOWN)
        nivel_escolar = Tex(NIVEL_ESCOLAR)
        nivel_escolar.next_to(comp_curricular,DOWN)
        professor_responsavel = Tex(PROFESSOR_RESPONSAVEL)
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
        #Unidade didatica/bases legais/habilidades bncc
        plano = Tex(r"Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        unidade_didatica = Tex(UNIDADE_DIDATICA)
        bases_legais = Tex(BASES_LEGAIS)
        bases_legais.next_to(unidade_didatica,DOWN)
        
        #justify
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")        
        habilidade_bncc = Tex(HABILIDADE_BNCC, tex_template=myTemplate, tex_environment="justify")
        habilidade_bncc.next_to(bases_legais,DOWN)
                
        
        slied1_group = VGroup(unidade_didatica,bases_legais,habilidade_bncc)
        slied1_group.scale(0.65)
        slied1_group.move_to(LEFT+UP)
        slied1_group.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(slied1_group))

        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
     
     
        
class slide3(Slide):
    def construct(self):
        #objetivos
        plano = Tex(r"Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")  
        obj = Tex(OBJETIVOS, tex_template=myTemplate, tex_environment="justify")
        obj.scale(0.65)
        obj.move_to(UP)
        self.play(Write(obj))
        

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
        
        
        
class slide4(Slide):
    def construct(self):
        #resursos didaticos/metodologia/tempo previsto/conteudo curricular/pre-requisitos curriculares/avaliação
        plano = Tex(r"Plano de aula",font_size=30)
        plano.move_to(UP*3 + LEFT*5)
        self.play(Write(plano))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}") 
        
        rec_dida = Tex(RECURSOS_DIDATICOS, tex_template=myTemplate, tex_environment="justify")
        meto = Tex(METODOLOGIA, tex_template=myTemplate, tex_environment="justify")
        tempo = Tex(TEMPO_PREVISTO, tex_template=myTemplate, tex_environment="justify")
        conte = Tex(CONTEUDO_CURRICULAR, tex_template=myTemplate, tex_environment="justify")
        prereq = Tex(PRE_REQUISITOS_CURRICULARES, tex_template=myTemplate, tex_environment="justify")
        ava = Tex(AVALIACAO, tex_template=myTemplate, tex_environment="justify")
        
        
        
        slied1_group = VGroup(rec_dida,meto,tempo,conte,prereq,ava)
        slied1_group.scale(0.65)
        slied1_group.move_to(UP*2)
        slied1_group.arrange(DOWN,center=False,aligned_edge=LEFT)
        self.play(Write(slied1_group))
        

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
        


class slide5(Slide):
    def construct(self):
        #Etapa 1
        plano = Tex(r"Plano de aula - Etapa 1: 10-20 minutos",font_size=25)
        plano.move_to(UP*3.5 + LEFT*4)
        self.play(Write(plano))
        
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}") 
        
        topico1 = Tex(r"$\bullet$Iniciar com a construção de diversos triângulos diferentes na lousa, e introduzir o conceito de semelhança.", tex_template=myTemplate, tex_environment="justify")
        topico1.scale(0.65)
        topico1.shift(UP*2)
        self.play(Write(topico1))
        self.pause()
        
        p1 = np.array([0,0,0])
        p2 = np.array([5,0,0])
        p3 = np.array([2.5,5,0])     
        
        tri1 = Polygon(p1,p2,p3)
        tri1.set_fill(BLUE,0.3)
        tri1.set_color(BLUE)
        angle1 = Angle.from_three_points(p1,p2,p3,other_angle=True).set_color(RED)
        angle2 = Angle.from_three_points(p1,p3,p2,other_angle=False).set_color(ORANGE)
        angle3 = Angle.from_three_points(p2,p1,p3,other_angle=False).set_color(GREEN)
        label1 = Tex(r"a")
        label1.next_to(tri1,LEFT)
        label1.shift(RIGHT*0.4)
        
        label2 = Tex(r"b")
        label2.next_to(tri1,RIGHT)
        label2.shift(LEFT*0.4)
        
        label3 = Tex(r"c")
        label3.next_to(tri1,DOWN)
        
        angle_label1 = Tex(r"x").set_color(RED)
        angle_label1.next_to(angle1,UL,buff=0.1)
        angle_label2 = Tex(r"y").set_color(ORANGE)
        angle_label2.next_to(angle2,DOWN)
        angle_label3 = Tex(r"z").set_color(GREEN)
        angle_label3.next_to(angle3,UR,buff=0.1)
        
        triangle1 = VGroup(tri1,angle1,angle2,angle3,label1,label2,label3,angle_label1,angle_label2,angle_label3)
        triangle1.scale(0.45)
        triangle1.move_to(np.array([-2,-1,0]))



        tri2 = Polygon(p1,p2,p3)
        tri2.set_fill(YELLOW,0.3)
        tri2.set_color(YELLOW)
        angle4 = Angle.from_three_points(p1,p2,p3,other_angle=True).set_color(RED)
        angle5 = Angle.from_three_points(p1,p3,p2,other_angle=False).set_color(ORANGE)
        angle6 = Angle.from_three_points(p2,p1,p3,other_angle=False).set_color(GREEN)
        label4 = Tex(r"a'")
        label4.next_to(tri2,LEFT)
        label4.shift(RIGHT*0.4)
        
        label5 = Tex(r"b'")
        label5.next_to(tri2,RIGHT)
        label5.shift(LEFT*0.4)
        
        label6 = Tex(r"c'")
        label6.next_to(tri2,DOWN)
        
        angle_label4 = Tex(r"x'").set_color(RED)
        angle_label4.next_to(angle4,UL,buff=0.1)
        angle_label5 = Tex(r"y'").set_color(ORANGE)
        angle_label5.next_to(angle5,DOWN)
        angle_label6 = Tex(r"z'").set_color(GREEN)
        angle_label6.next_to(angle6,UR,buff=0.1)
        
        triangle2 = VGroup(tri2,angle4,angle5,angle6,label4,label5,label6,angle_label4,angle_label5,angle_label6)
        triangle2.scale(0.7)
        triangle2.move_to(np.array([2,-1,0]))

        
        self.play(Write(tri1))
        self.pause()
        self.play(Write(label1),Write(label2),Write(label3))
        self.pause()
        self.play(Write(angle1),Write(angle2),Write(angle3),Write(angle_label1),Write(angle_label2),Write(angle_label3))
        self.pause()
        self.play(Write(triangle2))
        self.pause()
        
        triangles = VGroup(triangle1,triangle2)
        triangles.generate_target()
        triangles.target.shift(LEFT*2)
        self.play(MoveToTarget(triangles))
        
        lados = Tex(r"$\frac{a}{a'}=\frac{b}{b'}=\frac{c}{c'}=k$")
        lados.next_to(triangle2,RIGHT)
        lados.shift(RIGHT*0.8)
        self.play(Write(lados))
        self.pause()
        
        lados.generate_target()
        lados.target.shift(UP*2)

        angulos1 = Tex(r"$m(x)=m(x')$")
        angulos2 = Tex(r"$m(y)=m(y')$")
        angulos3 = Tex(r"$m(z)=m(z')$")
        
        angulos_m = VGroup(angulos1,angulos2,angulos3)
        angulos_m.arrange(DOWN)
        angulos_m.scale(0.8)
        angulos_m.next_to(lados.target,DOWN)
        angulos_m.shift(DOWN)
        
        
        self.play(MoveToTarget(lados))
        self.play(Write(angulos_m))
        
        self.pause()
        self.play(FadeOut(angulos_m),FadeOut(lados),FadeOut(triangles),FadeOut(topico1))
        
        topico2 = Tex(r"$\bullet$Diferenciar triângulos congruentes de triângulos semelhantes, podendo fazer uso da semântica das palavras, para tornar a diferença mais clara.", tex_template=myTemplate, tex_environment="justify")
        topico3 = Tex(r"$\bullet$Apresentar os casos de semelhança(ângulo-ângulo-ângulo, Lado-ângulo-Lado, Lado-Lado-Lado) através de figuras desenhadas na lousa pelo professor.", tex_template=myTemplate, tex_environment="justify")

        topicos = VGroup(topico2,topico3).arrange(DOWN,center=False,aligned_edge=LEFT)
        topicos.scale(0.65)
        topicos.shift(UP*2)
        self.play(Write(topicos))
        
        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()      
        
        

class slide6(Slide):
    def construct(self):
        #Etapa 2
        plano = Tex(r"Plano de aula - Etapa 2: 20-30 minutos",font_size=25)
        plano.move_to(UP*3.5 + LEFT*4)
        self.play(Write(plano))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}") 
        
        topico1 = Tex(r"$\bullet$Resolver de os seguintes 2 exercícios na lousa para posteriormente aplicar uma lista de 5 exercícios para resolução individual ou em grupo por parte dos alunos.", tex_template=myTemplate, tex_environment="justify")
        topico1.scale(0.65)
        topico1.shift(UP*2)
        self.play(Write(topico1))
        self.pause()
        
        exe = Tex(r"Exercício 1: A rampa de um hospital tem na sua parte mais elevada uma altura de 2,2 metros. Um paciente ao caminhar sobre a rampa percebe que se deslocou 3,2 metros e alcançou uma altura de 0,8 metro. Qual a distância em metros que o paciente ainda deve caminhar para atingir o ponto mais alto da rampa.", tex_template=myTemplate, tex_environment="justify")
        exe.scale(0.65)
        self.play(Write(exe))
        self.pause()
        
        self.play(FadeOut(exe),FadeOut(topico1))
        self.pause()
        
        exe2 = Tex(r"Exercício 2: O dono de um sítio pretende colocar uma haste de sustentação para melhor firmar dois postes de comprimentos iguais a 6 m e 4 m. A figura representa a situação real na qual os postes são descritos pelos segmentos AC e BD e a haste é representada pelo segmento EF, todos perpendiculares ao solo, que é indicado pelo segmento de reta AB. Os segmentos AD e BC representam cabos de aço que serão instalados.", tex_template=myTemplate, tex_environment="justify")
        exe2.scale(0.65)
        exe2.shift(UP*2)
        self.play(Write(exe2))
        
        ponto_a = Dot(np.array([0,0,0]))
        ponto_a_label = Tex(r"A")
        ponto_a_label.next_to(ponto_a,DOWN)
        
        ponto_b = Dot(np.array([10,0,0]))
        ponto_b_label = Tex(r"B")
        ponto_b_label.next_to(ponto_b,DOWN)
        
        ponto_c = Dot(np.array([0,4,0]))
        ponto_c_label = Tex(r"C")
        ponto_c_label.next_to(ponto_c,UP)
        
        ponto_d = Dot(np.array([10,6,0]))
        ponto_d_label = Tex(r"D")
        ponto_d_label.next_to(ponto_d,UP)
        
        ponto_f = Dot(np.array([4,0,0]))
        ponto_f_label = Tex(r"F")
        ponto_f_label.next_to(ponto_f,DOWN)
        
        ponto_e = Dot(np.array([4,2.4,0]))
        ponto_e_label = Tex(r"E")
        ponto_e_label.next_to(ponto_e,UP)
        
        line1 = Line(ponto_a.get_center(),ponto_c.get_center()).set_color(GRAY)
        line1_label = Tex(r"4")
        line1_label.next_to(line1,LEFT)
        line2 = Line(ponto_e.get_center(),ponto_f.get_center()).set_color(GRAY)
        line3 = Line(ponto_b.get_center(),ponto_d.get_center()).set_color(GRAY)
        line3_label = Tex(r"6")
        line3_label.next_to(line3,RIGHT)
        
        line4 = Line(ponto_c.get_center(),ponto_b.get_center()).set_color(WHITE)
        line5 = Line(ponto_a.get_center(),ponto_d.get_center()).set_color(WHITE)
        line6 = Line(ponto_a.get_center(),ponto_b.get_center()).set_color(WHITE)
        
        figura = VGroup(ponto_a,ponto_a_label,ponto_b,ponto_b_label,ponto_c,ponto_c_label,ponto_d,ponto_d_label,ponto_e,ponto_e_label,ponto_f,ponto_f_label,line1,line2,line3,line4,line5,line6,line1_label,line3_label)
        figura.scale(0.4)
        figura.move_to(np.array([0,-1,0]))
        self.play(Write(figura))
        self.pause()
        
        figura.generate_target()
        figura.target.shift(UP*0.5)
                
        exe2_2 = Tex(r"Qual deve ser o valor do comprimento da haste EF ?")
        exe2_2.scale(0.65)
        exe2_2.move_to(np.array([0,-3,0]))
        
        self.play(MoveToTarget(figura), Write(exe2_2))

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()   
        

class slide7(Slide):
    def construct(self):
        #Referencias
        plano = Tex(r"Referências",font_size=25)
        plano.move_to(UP*3.5 + LEFT*4)
        self.play(Write(plano))
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        ref1 = Tex(r"[1] GOUVEIA, Rosimar. $\textbf{Semelhança de Triângulos}$. [S. l.], [s. d.]. Disponível em: https://www.todamateria.com.br/semelhanca-de-triangulos/. Acesso em: 26 nov. 2022.‌", tex_template=myTemplate, tex_environment="justify")
        ref2 = Tex(r"[2] LUIZ, Robson. $\textbf{Semelhança de triângulos: teorema, casos, exemplos}$. [S. l.], [s. d.]. Disponível em: https://mundoeducacao.uol.com.br/matematica/semelhanca-triangulos.htm. Acesso em: 26 nov. 2022.‌", tex_template=myTemplate, tex_environment="justify")
        ref4 = Tex(r"[3] LIMA, E. L. et al. $\textbf{A Matemática do Ensino Médio}$. Rio de Janeiro: SBM, 2016, p. 1-4. (Coleção do Professor de Matemática). 130", tex_template=myTemplate, tex_environment="justify")
        
        referencias = VGroup(ref1,ref2,ref4).arrange(DOWN,center=False,aligned_edge=LEFT,buff=1.5)
        referencias.scale(0.50)
        referencias.shift(UP*3)
        
        self.play(Write(referencias))
        
        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait() 
