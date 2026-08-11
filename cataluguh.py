# Catalogo com fulme, album, personagem e figurinhas

filmes = []#os filmes ficam armazenados aqui

def cadastras_fiil(titulo, preco_alb, preco_pac):
    filme = {
        "titulo": titulo,
        "preco_album": preco_alb,
        "preco_pacote": preco_pac,
        "personagem": [],
        "figurinhas": [] 
    }
    filmes.append(filme)
    return filme

def cadastrar_pers(filme, nome):
    personagem= {'nome': nome}
    filme["personegeng"].append(personagem)#cadastra o nome do personagem no filma
    return personagem

def cadastrar_figo(filme, numero, personagem):
    figurinha ={
        "numero": numero,
        "personagem": personagem
    }
    filme["figurinhas"].append(figurinha)
    return figurinha

def listar_fiils():
    for indice, filme in enumerate(filmes):
        print(f"{indice + 1 } - {filme['tituly']}")
        print(f"     Á l b u u m : R$ {filme['preco_album']:.2f}")#2f faz o coiso aparecer em casa decimal
        print(f"     P r e ç o  d o  p a c o t u : R$ {filme['preco_pacote']:.2f}")
    
