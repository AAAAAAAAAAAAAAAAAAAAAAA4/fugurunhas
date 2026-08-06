# Catalogo com fulme, album, personagem e figurinhas.###

filmes = []

def cadastras_fiil(titulo, preco_al, preco_pac):
    filme = {
        "titulo": titulo,
        "preco album": preco_al,
        "preco_pacote": preco_pac,
        "personagem": [],
        "figurinhas": []
    }
    filmes.append(filme)
    return filme
def cadastrar_pers(filme, nome):
    filme["personegeng"].append(nome)

def cadastrar_figo(filme, numero, personagem)
    figurinha ={
        "numero": numero,
        "personagem": personagem
    }
    filme["figurinhas"].append(figurinha)