'''
Forma padrao do dict: {'Fulano': [10.0,8.9,9.9] , 'Beltrano': [7.2,2.5,5.2]}
Input esperado: Nome nota1 nota2 nota3
'''
if __name__ == '__main__':
    print("Entre com a quantidade de alunos: ")
    try:
        n = int(input())
    except Exception as ex:
        print("Ocorreu um erro na obtencao da quantidade de alunos - entre com um numero inteiro")
        exit()
    student_marks = {}

    # Criacao dos dados
    for _ in range(n):
        print("Insira o nome do aluno e suas tres notas separadas por espaco")
        name, *line = input().split() #input - espera conteudo do console, split separa o conteudo a cada espaco
        if len(line) != 3:
            print("Usuario deve entrar com tres notas")
            exit()
        scores = list(map(float, line))
        student_marks[name] = scores
    print("Entre com o nome do aluno que deseja obter a media: ")
    query_name = input() # nome do aluno que eu quero saber a nota

    if query_name in student_marks.keys():
        print ( 'Nome do aluno: ',query_name)
        print('Notas do aluno:',student_marks[query_name])
        soma = 0
        for valor in student_marks[query_name]:
            soma = soma + valor
        media = soma/len(student_marks[query_name])

        print('Media das notas: ',media)
    else:
        print('O usuario nao foi enontrado ',query_name)
