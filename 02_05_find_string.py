'''
Encontre uma String
Nesse desafio, o usuário entrará com uma string e uma substring.
Você tem de imprimir o número de vezes que a substring ocorre na string dada.
É assumido que você vai percorrer a string da esquerda para direita.

NOTE: A o problema é case-sensitive.

Formato de Entrada
A primeira linha da entrada contém a string original. A segunda linha contém a substring.

Formato de Entrada
Imprima o número inteiro indicando o total de ocorrências da substring na original.

Exemplo de Entrada 0
ABCDCDC
CDC
Exemplo de Saída 0
2
'''

def count_substring(string, sub_string):
    tam_sub_string = len (sub_string)
    resto = string
    result = 0
    count = resto.find(sub_string)
    while count >= 0:
        result += 1
        posicaoCorte = count + 1
        resto = resto[posicaoCorte:]
        count = resto.find(sub_string)
    return result

if __name__ == '__main__':
    print('Entre com uma frase:')
    string = input().strip()
    print ('Entre com um padrao')
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
