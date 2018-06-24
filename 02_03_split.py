def split_and_join(line):
    # write your code here
    result = line.split()
    result = "-".join(result)
    print(result)
    return result

def funcao_maceteada(line):
    return line.replace(' ','-')

if __name__ == '__main__':
    print("Digite uma frase: ")
    line = input()
    result = split_and_join(line)
    print("Resultado substituindo espaco por traco")
    print(result)
