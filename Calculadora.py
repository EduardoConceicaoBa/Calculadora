# Projeto prático Calculadora
class Calculadora:
    def somar(self,a, b):
        return a + b 
    
    def subtrair(self,a, b):
        return a - b

    def multiplicar(self,a, b):
        return a * b 

    def dividir(self,a, b):
        if b == 0:
            return "ERRO: Divisão por zero não é permitida"
        return a / b
def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    return input ("Escolha uma opção: ")

def main():
    calc = Calculadora()
    while True:
        opcao = menu()

        if opcao == "0":
            print("Encerrando a calculadora. Até mais! ")
            break
        if opcao not in ["1","2","3","4"]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            n1 = float(input("Escolha o primeiro número: "))
            n2 = float(input("Escolha o segundo número: "))
        except ValueError:
            print("ERRO: Digite apenas números válidos")
            continue

        if opcao == "1":
            resultado = calc.somar(n1,n2)
            print(f"Resultado da soma: {resultado}")

        elif opcao == "2":
            resultado = calc.subtrair(n1,n2)
            print(f"Resultado da subtração: {resultado}")

        elif opcao == "3":
            resultado = calc.multiplicar(n1,n2)
            print(f"Resultado da multiplicação: {resultado}")

        elif opcao == "4":
            resultado = calc.dividir(n1,n2)
            print(f"Resultado da divisão: {resultado}")
            
# Ponto de entrada do programa
main()