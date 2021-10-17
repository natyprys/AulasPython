class Carro:
    pass

#isinstance
meu_carro = Carro()

carro_do_ime = Carro()
#dois objetos em locais de memória diferentes

meu_carro.ano = 1968
meu_carro.modelo = "Fusca"
meu_carro.cor = "Azul"

carro_do_ime.ano = 1981
carro_do_ime.modelo = "Brasília"
carro_do_ime.cor = "Amarelo"

novo_fusca = meu_carro
novo_fusca.ano += 10

print (novo_fusca.ano)