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
        
               
        
        
        
        
        
        
        #slied1_group = VGroup()
        #slied1_group.scale(0.65)
        #slied1_group.move_to(UP*2)
        #slied1_group.arrange(DOWN,center=False,aligned_edge=LEFT)
        #self.play(Write(slied1_group))
        

        self.pause()
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()   
