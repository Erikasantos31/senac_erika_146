#dicionario

maca_vermelha = {
    'nome': 'Maçã',
    'cor': 'Vermelha'

}

maca_verde = {
    'nome': 'Maçã',
    'cor': 'Verde'
}
# type é para saber que tipo esta classificado sua variavel (str, inteiro, etc ....)
print(type(maca_verde), maca_vermelha)
print(maca_verde)

print(maca_vermelha['nome'], maca_vermelha['cor'])

maca_vermelha['preco'] = 1.99
print(maca_vermelha)

maca_vermelha['peso'] = '100 gramas'# para editar chama a variavel, coloca o que quer editar e a nova informação,e ao imprimir
print(maca_vermelha)                 # ja sai o novo valor editado

maca_vermelha['cor'] = ' ' #aspas '' significa remover apenas a cor e não o atributo (cor vemelha)
print(maca_vermelha)

del maca_vermelha['cor']  #del ele serve para remover um atributo que esta dentro do dicionario, no caso (cor vermelha)
print(maca_vermelha)

