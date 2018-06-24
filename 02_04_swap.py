def swap_case(s):
    result = ""
    for letra in s:
        if letra >= 'a' and letra <= 'z':
            result += letra.upper() # result = result + letra.upper()
        elif letra >= 'A' and letra <= 'Z':
            result += letra.lower()
        else:
            result += letra
    return result

if __name__ == '__main__':
    print('Entre com uma frase:')
    s = input()
    result = swap_case(s)
    print(result)
