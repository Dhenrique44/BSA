class Equipe:
    def __init__(self, nome, idade, estadio, formacao, jogadores):
        self.nome = nome
        self.idade = idade
        self.estadio = estadio
        self.formacao = formacao
        self.jogadores = jogadores


    def imprimirInformacoes (self):
        selectInfo = input("Digite:\n"
                           "1 Nome \n"
                           "2 Idade \n"
                           "3 Estadio \n"
                           "4 Formação \n"
                           "5 Elenco \n")
        if selectInfo == '1':
            print("Nome: ", self.nome )
        elif selectInfo == '2':
            print("Idade: ", self.idade)
        elif selectInfo == '3':
            print("Estadio: ", self.estadio)
        elif selectInfo == '4':
            print("Formacao: ", self.formacao)
        elif selectInfo == '5':
            print("Elenco:")
            for jogador in self.jogadores:
                print(jogador)

AtP = Equipe(
    nome= "Club Athletico Paranaense",
    idade= 100,
    estadio= " Ligga Arena",
    formacao= 4_2_3_1,
    jogadores= ["GL Bento", "ZG K. Rocha", "VL Fernandinho", "LE Fernando", "AT Gonzalo M.", "MC B. Zapelli", "AT R. Benitez", "AT A. Cannobio", "ZG Gamarra", "AT Jader", "AT Julimar", "MC Nikão", "LD Madson", "GL Leo L.", "VL Erick", "MC Thomas K.", "LD L. Godoy", "LE Ezquivel", "GL Mykael", "GL G. Pereira", "ZG T. Heleno", "VL Alex S.", "MC Christian", "AT Pablo", "VL Gabriel"],
)
AtG = Equipe(
    nome= "Atlético Clube Goianiense",
    idade= 87,
    estadio= " Estádio Antonio Accioly",
    formacao= 4_2_3_1,
    jogadores= ["GL", "Ronaldo", "P. Rangel","" , "DF", "P. Henrique", "L. Felipe", "A. Martins", "J. Victor", "B. Tubarão", "Maguinho", "G. Romão", "Y. Rodallega", "", "MC:", "Roni", "Rhaldney", "L. Kal", "Campanharo", "B. Santos", "Danielzinho", "Shaylon", "Ángelo A.", "", "AT:", "Alejo C.", "M. Zuleta", "Luiz F.", "Yony G.", "G. Barros", "E. Rodríguez", "V. Love", "Max", "Derek"],
)
AtM = Equipe(
    nome= "Clube Atlético Mineiro",
    idade= 116,
    estadio= "Arena MRV",
    formacao= 3_4_3,
    jogadores= ["GL G. Delfim", "ZG B. Fuchs", "ZG M. Lemos", "VL Otávio", "MC G. Scarpa", "AT Hulk", "AT Paulinho", "AT E. Vargas", "LE G. Arana", "AT A. Kardec", "MC M. Zaracho", "ZG I. Rabello", "GL Éverson", "VL A. Franco", "LD Mariano", "LD R. Saravia", "ZG Jemerson", "MC Pedrinho"],
)
Bah = Equipe(
    nome="Esporte Clube Bahia",
    idade= 93,
    estadio="Arena Fonte Nova",
    formacao= 4_1_2_1_2,
    jogadores=["G Danilo Fernandes", "LD Gilberto", "Z Gabriel Xavier", "Z Kanu", "V Rezende", "V Jean Lucas", "A Ademir", "MC Cauly","AT Everaldo", "MC É. Ribeiro ", "AT Biel", "LD S. Arias", "MC C. Pena", "ZG V. Cuesta", "MC Thaciano", "VL C. Alexandre", "VL N. Acevedo", "MC Y. Felipe", "LD Cicinho"],
)
Bot = Equipe(
    nome="Botafogo de Futebol e Regatas",
    idade=119,
    estadio="Nilton Santos",
    formacao=4_2_3_1,
    jogadores=["GL G. Fernández", "LD Rafael", "ZG L. Halter", "LD Mateo Ponte", "VL D. Barbosa", "VL Tchê Tchê", "AT L. Henrique", "VL P. Paula", "AT T. Soares", "AT J. Savarino", "AT J. Santos", "GL John", "ZG Bastos", "LE Marçal", "LD D. Suárez", "ZG Pablo", "VL Gregore", "MC Eduardo", "MC Ó. Romero", "AT M. Nascimento"],
)
Cor = Equipe(
    nome="Sport Clube Corinthians Paulista",
    idade=113,
    estadio="Neo Química Arena",
    formacao=4_3_3,
    jogadores=["LD Matheuzinho", "ZG F. Torres", "VL F. Vera", "LE D. Palacios", "VL Maycon", "VL Paulinho", "AT Yuri A.", "MC R. Garro", "AT Á. Romero", "GL Cássio", "ZG G Henrique", "VL Raniele", "AT P. Henrique", "AT G. Silva", "AT P. Raul", "LE M. Bidu", "GL C. Miguel", "LD Fagner", "ZG Cacá", "MC G. Biro", "GL Donell", "LE	Hugo", "MC I. Coronado"],
)
Cri = Equipe(
    nome="Criciúma Esporte Clube",
    idade=76,
    estadio="Heriberto Hülse",
    formacao=4_4_2,
    jogadores=["GL:", "Alisson", "M. Teixeira", "Kauã", "", "DF:", "Claudinho", "Jonathan", "W. Maia", "Rodrigo", "W. Ángel", "T. Figueiredo", "M. Hermes", "M. Trauco", "", "MC:", "Barreto", "Higor Meritão", "Mateo Barcia", "Eliedson", "M. Gabriel", "Y. Candelo", "F. Mateus", "Matheusinho", "", "AT:", "Éder", "F. Vizeu", "Y. Bolasie", "R. Kayzer", "J. Carlos", "E. Melo"]
)
Cru = Equipe(
    nome="Cruzeiro Esporte Clube",
    idade=103,
    estadio="Mineirão",
    formacao=4_3_3,
    jogadores=["GL:", "Rafael Cabral", "Anderson", "","DF:", "Neris", "L. Oliveira", "J. Marcelo", "Z. Ivaldo", "", "Willian", "Wesley", "Marlon", "Kaiki", "", "MC:", "L. Romero", "L. Silva", "I. Luccas", "Ramiro", "M. Pereira", "M. Vital", "", "AT:", "Wesley","A. Gomes", "G. Veron", "J. Dinenno", "R. Silva "],
)
Cui = Equipe(
    nome="Cuiabá Esporte Clube",
    idade=23,
    estadio=" Arena Pantanal",
    formacao=4_3_3,
    jogadores=["GL:", "Walter", "J. Carlos", "", "DF:", "Marllon", "A. Empereur", "A. Conceição", "Hayner", "I. Cariús", "M. Alexandre", "Rikelme", "", "MC:", "Camilo", "Uendel", "L. Cardoso", "Pepê", "Ronald", "", "AT:", "Pitta", "J. Cafu", "F. Marques", "A. Luís", "W. Silva"],
)
Fla = Equipe(
    nome="Clube de Regatas Flamengo",
    idade=128,
    estadio="Maracanã",
    formacao=4_2_3_1,
    jogadores=["GL:", "A. Rossi", "M. Cunha", "", "DF:", "Léo P.", "F. Bruno", "D. Luiz", "L. Ortiz", "G. Varela", "Wesley", "Ayrton L.", "M. Viña", "", "MC:", "Pulga", "Allan", "Arrascaeta", "De La Cruz", "Gerson", "", "AT:", "Gabigol", "Pedro", "B. Henrique", "E. Cebolinha", "Luiz A."],
)
Flu = Equipe(
    nome="Fluminense Footbaal Club",
    idade=121,
    estadio="Laranjeiras",
    formacao=4_2_3_1,
    jogadores=["GL:", "Fábio", "F. Alves", "", "DF:", "S. Xavier", "Guga", "F. Melo", "Nino", "D. Braz", "Marlon", "Marcelo", "D. Barbosa", "", "MC:", "André", "T. Santos", "Alexsander", "Martinelli", "P. H. Ganso", "R. Augusto", "D. Terans", "Lima", "", "AT:", "G. Cano", "J. Arias", "J. Kennedy", "Keno", "D. Costa"],
)
For = Equipe(
    nome="Fortaleza Esporte Clube",
    idade=105,
    estadio="Arena Castelão",
    formacao=4_4_2,
    jogadores=["GL:", "J. Ricardo", "Santos", "", "DF", "Tinga", "Dudu", "Titi", "E. Brítez", "T. Cardona", "B. Kuscevic", "Geilson", "B. Pacheco", "F. Jonatan", "", "MC:", "Z. Welison", "L. Sasha", "Y. Pikachu", "Tomás P.", "Luquinhas", "Calebe", "", "AT:", "Marinho", "Thiago G.", "P. Rocha", "B. Lopes", "I. Machuc"],
)
Gre = Equipe(
    nome="Grêmio Foot-Ball Porto Alegrense",
    idade=120,
    estadio="Arena do Grêmio",
    formacao=4_4_3,
    jogadores=["GL:", "A. Marchesín", "C. Santos", "", "DF:", "J. Pedro", "Fábio", "Geromel", "R. Ely", "Kannemann", "G. Martins", "Reinaldo", "Mayk", "", "MC:", "Du Queiroz", "Edenílson", "M. Villasanti", "Dodi", "Cristaldo", "Nathan", "Pepê", "", "AT:", "Diego C.", "Soteldo", "Pavón", "Galdino", "Besozzi"],
)
Int = Equipe(
    nome="Sport Club Internacional",
    idade=115,
    estadio="Estádio Beira-Rio",
    formacao=4_4_2,
    jogadores=["GL:","S. Rochet", "Anthoni", "","DF:", "F. Bustos", "H. Mallo", "Vitão", "R. Renan", "G. Mercado", "I. Gomes", "Renê", "A. Bernabei", "", "MC:", "B. Henrique", "Rômulo", "B. Gomes", "T. Maia", "Alan P.", "Aránguiz", "Maurício", "Hyoran", "", "AT:", "Valencia", "Borré", "Alario", "Luiz A."],
)
Juv = Equipe(
    nome= "Esporte Clube Juventude",
    idade= 110,
    estadio= " Estádio Alfredo Jaconi",
    formacao= 4_2_3_1,
jogadores= ["GL:", "Gabriel", "L. Wingert", "", "DF:", "A. Ruschel", "Danilo", "Ewerton", "Gabriel", "J. Lucas", "J. Vitor", "L. Freitas", "R. Sam", "", "MC:", "Caique", "Jean Carlos", "Jádson", "Kelvi", "Nenê", "Peixoto", "Rafinha", "", "AT:", "", "Bill", "Edson", "Erick", "Gilberto", "Kleiton", "Marcelinho", "Rildo"],
)
Pal = Equipe(
    nome="Sociedade Esportiva Palmeiras",
    idade=109,
    estadio="Allianz Park",
    formacao=4_2_2_2,
    jogadores=["GL:", "Weverton", "M. Lomba", "", "DF:", "Murilo", "G Gómez", "Luan", "Piquerez", "Vanderlan", "Paulista", "Mayke", "M. Rocha", "", "MC:", "Aníbal", "G. Menino", "Zé Rafael", "R. Ríos", "Veiga", "Rômulo", "", "AT:", "Dudu", "Endrick", "Rony", "Breno", "Artur", "López"],
)
Rbb = Equipe(
    nome="Red Bull Bragantino",
    idade=96,
    estadio="Estádio Nabi Abi Chedid",
    formacao=4_4_3,
    jogadores=["GL:", "Cleiton", "Lucão", "", "DF:", "Henrique", "Cunha", "Realpe", "Mendes", "Cândido", "Capixaba", "Hurtado", "Nathan", "", "MC:", "Jadsom", "Fernandes", "Ramires", "Evangelista", "Lincoln", "Vitinho", "", "AT:", "Vitinho"],
)
Spl = Equipe(
    nome="São Paulo Futebol Clube",
    idade=94,
    estadio="MorumBIS",
    formacao=4_2_3_1,
    jogadores=["GL:", "Rafael", "Jandrei", "", "DF:", "Rafinha", "I. Vinícius", "Arboleda", "Franco", "Ferraresi", "D. Costa", "Welington", "Patryck", "", "MC:", "L. Gustavo", "P. Maia", "R. Nestor", "G. Neves", "Alisson", "Bobadilla", "Galoppo", "", "AT:", "W. Rato", "Lucas", "Calleri", "Luciano", "Ferreira"],
)
Vas = Equipe(
    nome="Vasco da Gama",
    idade=125,
    estadio="Estádio São Januário",
    formacao=4_2_3_1,
    jogadores=["GL:", "L. Jardim", "Keiller", "", "DF:", "P. Henrique", "Puma R.", "Gary Medel", "J. Victor", "Léo", "Maicon", "L. Piton", "V. Luís", "", "MC:", "Z Gabriel", "Jair", "M. Carvalho", "Payet", "Galdames", "Praxedes", "", "AT:", "Vegetti", "Rossi", "David", "Adson", "Rayan"],
)
Vit = Equipe(
    nome="Vitória",
    idade=125,
    estadio="Barradão",
    formacao=3_4_1_2,
    jogadores=["GL:", "L. Arcanjo", "Muriel", "", "DF:", "W. Leonardo", "Reynaldo", "Camutanga", "Uvini", "Esteves", "PK", "Zeca", "Lepo", "", "MC:", "Santos", "Vinicius", "Andrade", "Oliveira", "Mota", "Daniel Jr", "", "AT:", "Everaldo", "M. Gonçalves", "Castillo", "Osvaldo", "Alerrandro", "Iury"],
)
opcao = input("Digite: \n"
              "1  Athletico Paranaense \n"
              "2 Atlético Goianiense \n"
              "3 Atlético Mineiro \n"
              "4 Bahia \n"
              "5 Botafogo \n"
              "6 Corinthians \n"
              "7 Criciúma \n"
              "8 Cruzeiro \n"
              "9 Cuiabá \n"
              "10 Flamengo \n"
              "11 Fluminense \n"
              "12 Fortaleza \n"
              "13 Grêmio \n"
              "14 Internacional \n"
              "15 Juventude \n"
              "16 Palmeiras \n"
              "17 Red Bull Bragantino \n"
              "18 São Paulo \n"
              "19 Vasco da Gama \n"
              "20 Vitória\n")

if opcao == '1':
    AtP.imprimirInformacoes()
elif opcao == '2':
    AtG.imprimirInformacoes()
elif opcao == '3':
    AtM.imprimirInformacoes()
elif opcao == '4':
    Bah.imprimirInformacoes()
elif opcao == '5':
    Bot.imprimirInformacoes()
elif opcao == '6':
    Cor.imprimirInformacoes()
elif opcao == '7':
    Cri.imprimirInformacoes()
elif opcao == '8':
    Cru.imprimirInformacoes()
elif opcao == '9':
    Cui.imprimirInformacoes()
elif opcao == '10':
    Fla.imprimirInformacoes()
elif opcao == '11':
    Flu.imprimirInformacoes()
elif opcao == '12':
    For.imprimirInformacoes()
elif opcao == '13':
    Gre.imprimirInformacoes()
elif opcao == '14':
    Int.imprimirInformacoes()
elif opcao == '15':
    Juv.imprimirInformacoes()
elif opcao == '16':
    Pal.imprimirInformacoes()
elif opcao == '17':
    Rbb.imprimirInformacoes()
elif opcao == '18':
    Spl.imprimirInformacoes()
elif opcao == '19':
    Vas.imprimirInformacoes()
elif opcao == '20':
    Vit.imprimirInformacoes()
else: print("Erro!")
