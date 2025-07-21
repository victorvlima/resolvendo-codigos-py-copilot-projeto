"""
Desafio: Operações Matemáticas Simples 📐
Múltiplas implementações para cálculos matemáticos
Autor: Victor Lima e Claude 4 Sonnet
"""

import math

def solucao_basica():
    """
    Versão 1: Operações básicas simples
    Soma, subtração, multiplicação e divisão
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    try:
        # Recebendo os números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realizando operações básicas
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        
        # Divisão com tratamento de zero
        if num2 != 0:
            divisao = num1 / num2
        else:
            divisao = "Indefinido (divisão por zero)"
        
        # Exibindo resultados
        print(f"\nResultados:")
        print(f"Soma: {num1} + {num2} = {soma}")
        print(f"Subtração: {num1} - {num2} = {subtracao}")
        print(f"Multiplicação: {num1} × {num2} = {multiplicacao}")
        print(f"Divisão: {num1} ÷ {num2} = {divisao}")
        
    except ValueError:
        print("❌ Por favor, digite números válidos!")


def solucao_com_menu():
    """
    Versão 2: Com menu de operações
    Usuário escolhe qual operação realizar
    """
    print("\n🔹 SOLUÇÃO COM MENU")
    print("-" * 30)
    
    try:
        # Recebendo os números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Menu de operações
        print("\n📋 Escolha a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (×)")
        print("4. Divisão (÷)")
        print("5. Potenciação (^)")
        print("6. Módulo (%)")
        
        opcao = input("Digite sua opção (1-6): ").strip()
        
        # Realizando a operação escolhida
        if opcao == "1":
            resultado = num1 + num2
            operacao = f"{num1} + {num2} = {resultado}"
        elif opcao == "2":
            resultado = num1 - num2
            operacao = f"{num1} - {num2} = {resultado}"
        elif opcao == "3":
            resultado = num1 * num2
            operacao = f"{num1} × {num2} = {resultado}"
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                operacao = f"{num1} ÷ {num2} = {resultado}"
            else:
                operacao = "❌ Erro: Divisão por zero!"
        elif opcao == "5":
            resultado = num1 ** num2
            operacao = f"{num1} ^ {num2} = {resultado}"
        elif opcao == "6":
            if num2 != 0:
                resultado = num1 % num2
                operacao = f"{num1} % {num2} = {resultado}"
            else:
                operacao = "❌ Erro: Módulo por zero!"
        else:
            operacao = "❌ Opção inválida!"
        
        print(f"\n✅ Resultado: {operacao}")
        
    except ValueError:
        print("❌ Por favor, digite números válidos!")


def solucao_robusta():
    """
    Versão 3: Calculadora completa e robusta
    Múltiplas operações, validações e funcionalidades extras
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    try:
        # Recebendo e validando números
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            except ValueError:
                print("❌ Número inválido! Tente novamente.")
        
        while True:
            try:
                num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("❌ Número inválido! Tente novamente.")
        
        # Realizando todas as operações
        operacoes = {}
        
        # Operações básicas
        operacoes["Soma"] = num1 + num2
        operacoes["Subtração"] = num1 - num2
        operacoes["Multiplicação"] = num1 * num2
        
        # Divisão com verificação
        if num2 != 0:
            operacoes["Divisão"] = num1 / num2
            operacoes["Divisão inteira"] = num1 // num2
            operacoes["Módulo"] = num1 % num2
        else:
            operacoes["Divisão"] = "Indefinido (÷0)"
            operacoes["Divisão inteira"] = "Indefinido (÷0)"
            operacoes["Módulo"] = "Indefinido (%0)"
        
        # Operações avançadas
        operacoes["Potenciação"] = num1 ** num2
        
        # Operações especiais
        if num1 >= 0:
            operacoes["Raiz quadrada do 1º"] = math.sqrt(num1)
        else:
            operacoes["Raiz quadrada do 1º"] = "Indefinido (√negativo)"
        
        if num2 >= 0:
            operacoes["Raiz quadrada do 2º"] = math.sqrt(num2)
        else:
            operacoes["Raiz quadrada do 2º"] = "Indefinido (√negativo)"
        
        # Comparações
        operacoes["Maior número"] = max(num1, num2)
        operacoes["Menor número"] = min(num1, num2)
        operacoes["Diferença absoluta"] = abs(num1 - num2)
        
        # Exibindo resultados organizados
        print("\n" + "="*60)
        print(f"🧮 CALCULADORA COMPLETA")
        print("="*60)
        print(f"📊 Números: {num1} e {num2}")
        print("-"*60)
        
        for nome, resultado in operacoes.items():
            if isinstance(resultado, float):
                if resultado.is_integer():
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 4)
            print(f"{nome:20} = {resultado}")
        
        print("="*60)
        
        # Informações extras
        print(f"\n📈 ANÁLISE ADICIONAL:")
        print(f"   • Soma dos quadrados: {num1**2 + num2**2}")
        print(f"   • Média aritmética: {(num1 + num2) / 2}")
        if num1 > 0 and num2 > 0:
            print(f"   • Média geométrica: {math.sqrt(num1 * num2):.4f}")
        print(f"   • Produto: {num1 * num2}")
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def calculadora_interativa():
    """
    Versão 4: Calculadora interativa contínua
    Permite múltiplos cálculos em sequência
    """
    print("\n🔹 CALCULADORA INTERATIVA")
    print("-" * 30)
    
    resultado_anterior = None
    
    while True:
        try:
            print(f"\n{'='*40}")
            print("🧮 CALCULADORA INTERATIVA")
            if resultado_anterior is not None:
                print(f"📊 Resultado anterior: {resultado_anterior}")
            print("="*40)
            
            # Opção de usar resultado anterior
            if resultado_anterior is not None:
                usar_anterior = input("Usar resultado anterior como primeiro número? (s/n): ").lower().strip()
                if usar_anterior == 's':
                    num1 = resultado_anterior
                    print(f"Primeiro número: {num1}")
                else:
                    num1 = float(input("Digite o primeiro número: "))
            else:
                num1 = float(input("Digite o primeiro número: "))
            
            # Segundo número
            num2 = float(input("Digite o segundo número: "))
            
            # Menu de operações
            print("\n📋 Operações disponíveis:")
            operacoes_menu = {
                '+': 'Soma',
                '-': 'Subtração', 
                '*': 'Multiplicação',
                '/': 'Divisão',
                '**': 'Potenciação',
                '%': 'Módulo',
                '//': 'Divisão inteira'
            }
            
            for simbolo, nome in operacoes_menu.items():
                print(f"   {simbolo:3} - {nome}")
            
            operador = input("\nDigite o operador: ").strip()
            
            # Realizando operação
            if operador == '+':
                resultado = num1 + num2
                operacao_str = f"{num1} + {num2}"
            elif operador == '-':
                resultado = num1 - num2
                operacao_str = f"{num1} - {num2}"
            elif operador == '*':
                resultado = num1 * num2
                operacao_str = f"{num1} × {num2}"
            elif operador == '/':
                if num2 != 0:
                    resultado = num1 / num2
                    operacao_str = f"{num1} ÷ {num2}"
                else:
                    print("❌ Erro: Divisão por zero!")
                    continue
            elif operador == '**':
                resultado = num1 ** num2
                operacao_str = f"{num1} ^ {num2}"
            elif operador == '%':
                if num2 != 0:
                    resultado = num1 % num2
                    operacao_str = f"{num1} % {num2}"
                else:
                    print("❌ Erro: Módulo por zero!")
                    continue
            elif operador == '//':
                if num2 != 0:
                    resultado = num1 // num2
                    operacao_str = f"{num1} // {num2}"
                else:
                    print("❌ Erro: Divisão inteira por zero!")
                    continue
            else:
                print("❌ Operador inválido!")
                continue
            
            # Formatando resultado
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            elif isinstance(resultado, float):
                resultado = round(resultado, 6)
            
            print(f"\n✅ {operacao_str} = {resultado}")
            resultado_anterior = resultado
            
            # Continuar?
            continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower().strip()
            if continuar != 's':
                break
                
        except ValueError:
            print("❌ Por favor, digite números válidos!")
        except KeyboardInterrupt:
            print("\n\n👋 Calculadora encerrada!")
            break


def comparar_operacoes():
    """
    Compara diferentes formas de realizar operações
    """
    print("\n🔄 COMPARAÇÃO DE OPERAÇÕES")
    print("="*50)
    
    try:
        # Coletando números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        print(f"\n🔍 COMPARANDO OPERAÇÕES COM: {num1} e {num2}")
        print("="*60)
        
        # Diferentes formas de potenciação
        print("🔢 POTENCIAÇÃO:")
        print(f"   Operador **: {num1} ** {num2} = {num1 ** num2}")
        print(f"   Função pow(): pow({num1}, {num2}) = {pow(num1, num2)}")
        print(f"   Math.pow(): math.pow({num1}, {num2}) = {math.pow(num1, num2)}")
        
        # Diferentes formas de divisão
        if num2 != 0:
            print(f"\n➗ DIVISÃO:")
            print(f"   Divisão real: {num1} / {num2} = {num1 / num2}")
            print(f"   Divisão inteira: {num1} // {num2} = {num1 // num2}")
            print(f"   Módulo: {num1} % {num2} = {num1 % num2}")
        
        # Operações com math
        print(f"\n📐 FUNÇÕES MATEMÁTICAS:")
        if num1 > 0:
            print(f"   log({num1}) = {math.log(num1):.4f}")
            print(f"   log10({num1}) = {math.log10(num1):.4f}")
        if num1 >= 0:
            print(f"   sqrt({num1}) = {math.sqrt(num1):.4f}")
        print(f"   abs({num1}) = {abs(num1)}")
        print(f"   ceil({num1}) = {math.ceil(num1)}")
        print(f"   floor({num1}) = {math.floor(num1)}")
        
    except ValueError:
        print("❌ Números inválidos!")
    except Exception as e:
        print(f"❌ Erro: {e}")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*60)
    print("📐 OPERAÇÕES MATEMÁTICAS SIMPLES - CALCULADORA")
    print("="*60)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ Operações fundamentais (+, -, ×, ÷)")
    print()
    print("2️⃣  Solução com Menu")
    print("    └─ Escolha a operação desejada")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Calculadora completa com análises")
    print()
    print("4️⃣  Calculadora Interativa")
    print("    └─ Múltiplos cálculos em sequência")
    print()
    print("5️⃣  Comparar Operações")
    print("    └─ Diferentes métodos de cálculo")
    print()
    print("6️⃣  Exemplos Práticos")
    print("    └─ Casos de uso interessantes")
    print()
    print("0️⃣  Sair")
    print("-" * 60)


def exemplos_praticos():
    """
    Demonstra casos de uso práticos
    """
    print("\n🎯 EXEMPLOS PRÁTICOS")
    print("="*50)
    
    exemplos = [
        (10, 3, "Cálculos básicos"),
        (25, 5, "Números que dividem exato"),
        (7, 0, "Divisão por zero"),
        (2, 8, "Potências de 2"),
        (9, 0.5, "Raiz quadrada usando potência"),
        (-5, 3, "Números negativos")
    ]
    
    for num1, num2, descricao in exemplos:
        print(f"\n📝 {descricao}: {num1} e {num2}")
        print(f"   Soma: {num1 + num2}")
        print(f"   Multiplicação: {num1 * num2}")
        if num2 != 0:
            print(f"   Divisão: {num1 / num2:.2f}")
        else:
            print(f"   Divisão: Indefinido")
        print(f"   Potência: {num1 ** num2}")
    
    # Calculadora de área
    print(f"\n🏠 CALCULADORA DE ÁREA (Retângulo):")
    try:
        largura = float(input("Digite a largura: "))
        altura = float(input("Digite a altura: "))
        area = largura * altura
        perimetro = 2 * (largura + altura)
        print(f"   Área: {area}")
        print(f"   Perímetro: {perimetro}")
    except ValueError:
        print("❌ Valores inválidos!")


def main():
    """
    Função principal que controla o fluxo do programa
    """
    while True:
        try:
            exibir_menu()
            opcao = input("Digite sua opção: ").strip()
            
            if opcao == "1":
                solucao_basica()
            elif opcao == "2":
                solucao_com_menu()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                calculadora_interativa()
            elif opcao == "5":
                comparar_operacoes()
            elif opcao == "6":
                exemplos_praticos()
            elif opcao == "0":
                print("\n👋 Obrigado por usar a Calculadora!")
                print("📐 Continue praticando matemática com Python! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar (exceto para calculadora interativa)
            if opcao in ["1", "2", "3", "5", "6"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar a Calculadora!")
                    print("📐 Continue praticando matemática com Python! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()