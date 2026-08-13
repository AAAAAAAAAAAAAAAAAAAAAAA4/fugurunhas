from cataluguh import (
    filmes,
    cadastras_fiil,
    cadastrar_pers,
    cadastrar_figo,
    listar_fiils,
    cadastrar_pacote


)
from vanda import realizar_venda, exibir_venda

witch_Hat_atelier=cadastras_fiil(titulo="Witch Hat Atelier", preco_albuu=10, preco_pacote=5)

#ajeitar depois(tudo para witch hat atelier)
Agati = cadastrar_pers( filme= witch_Hat_atelier, nome= "Agati")
Coco = cadastrar_pers( filme= witch_Hat_atelier, nome= "Coco")
Tetia = cadastrar_pers(filme= witch_Hat_atelier, nome= "Tetia")
Riche= cadastrar_pers(filme=witch_Hat_atelier, nome= "Riché")
Qifrey= cadastrar_pers(filme=witch_Hat_atelier, nome= "Qifrey")
Olruggio= cadastrar_pers(filme=witch_Hat_atelier, nome= "Olruggio")

fig1=cadastrar_figo(filme=witch_Hat_atelier, numero=1, personagem= Agati)
fig2=cadastrar_figo(filme=witch_Hat_atelier, numero=2, personagem= Coco)
fig3=cadastrar_figo(filme=witch_Hat_atelier, numero=3, personagem= Tetia)
fig4=cadastrar_figo(filme=witch_Hat_atelier, numero=4, personagem= Riche )
fig5=cadastrar_figo(filme=witch_Hat_atelier, numero=5, personagem= Qifrey )
fig6=cadastrar_figo(filme=witch_Hat_atelier, numero=6, personagem= Olruggio )

pacote1= cadastrar_pacote(fig1,fig2,fig3)
pacote2= cadastrar_pacote(fig2,fig5,fig3)
pacote3= cadastrar_pacote(fig3,fig6,fig5)
pacote4= cadastrar_pacote(fig5,fig6,fig4)
pacote5= cadastrar_pacote(fig3,fig6,fig2)
pacote6= cadastrar_pacote(fig4,fig6,fig2)

#listar_fiils()
venda = realizar_venda(witch_Hat_atelier, 1, [pacote1, pacote2, pacote3, pacote4, pacote5, pacote5, pacote6])
exibir_venda(venda)
