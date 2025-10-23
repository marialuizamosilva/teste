print ()
comando = "continuar"

while comando == "continuar":
    a = float(input("Digite um número: "))
    b = float(input("Digite um número: "))
soma = a + b
subtracao = a - b
print(f"O valor da soma dos números a e b é {soma:.2f}")
print(f"O valor da subtração dos números a e b é {subtracao:.2f}")
comando = input("Digite continuar para fazer outra soma ou parar para encerrar o programa: ")


