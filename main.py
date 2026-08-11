from cataluguh import (
    filmes,
    cadastrar_fiil,
    cadastrar_pers,
    cadastrar_figo,
    listar_fiils

)

serviço_de_entregas_da_kiki =cadastrar_fiil(titulo="Serviço de entregas da kiki", preco_albuu=16, preco_pacote=8)
bubble =cadastrar_fiil(titulo="Bubble", preco_albuu=17, preco_pacote=8)

Kiki = cadastrar_pers( filme= serviço_de_entregas_da_kiki, nome= "Kiki")
Uta = cadastrar_pers( filme= bubble, nome= "Uta")

fig1=cadastrar_figo(filme=serviço_de_entregas_da_kiki, numero=1, personagem= Kiki)
fig2=cadastrar_figo(filme=bubble, numero=2, personagem= Uta)

listar_fiils()