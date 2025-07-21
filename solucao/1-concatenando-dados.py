"""
Desafio: Concatenando Dados 🐾
Múltiplas implementações para concatenação de strings
Autor: Victor Lima e Claude 4 Sonnet
"""

def solucao_basica():
    """
    Versão 1: Implementação básica
    Concatenação simples sem formatação especial
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    # Recebendo os dados do usuário
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    # Concatenando os dados
    resultado = dado1 + dado2
    
    # Exibindo o resultado
    print("Resultado da concatenação:", resultado)


def solucao_com_espacamento():
    """
    Versão 2: Com espaçamento entre os dados
    Adiciona espaço automático entre os dados
    """
    print("\n🔹 SOLUÇÃO COM ESPAÇAMENTO")
    print("-" * 30)
    
    # Recebendo os dados do usuário
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    # Concatenando com espaço entre os dados
    resultado = dado1 + " " + dado2
    
    # Exibindo o resultado
    print(f"Resultado: {resultado}")


def solucao_robusta():
    """
    Versão 3: Implementação robusta
    Com validação, tratamento de erros e informações detalhadas
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    try:
        # Recebendo os dados
        dado1 = input("Digite o primeiro dado: ").strip()
        dado2 = input("Digite o segundo dado: ").strip()
        
        # Verificando se os dados não estão vazios
        if not dado1 and not dado2:
            print("⚠️ Ambos os dados estão vazios!")
            return
        
        # Perguntando sobre separador
        usar_separador = input("Deseja usar um separador? (s/n): ").lower().strip()
        
        if usar_separador == 's':
            separador = input("Digite o separador (ou pressione Enter para espaço): ")
            if not separador:
                separador = " "
            resultado = f"{dado1}{separador}{dado2}"
        else:
            resultado = f"{dado1}{dado2}"
        
        # Exibindo resultados detalhados
        print("\n" + "="*40)
        print(f"📝 Primeiro dado: '{dado1}' ({len(dado1)} chars)")
        print(f"📝 Segundo dado: '{dado2}' ({len(dado2)} chars)")
        print(f"✅ Resultado: '{resultado}'")
        print(f"📊 Tamanho final: {len(resultado)} caracteres")
        print("="*40)
        
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*50)
    print("🐾 CONCATENADOR DE DADOS - MÚLTIPLAS SOLUÇÕES")
    print("="*50)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ Concatenação simples e direta")
    print()
    print("2️⃣  Solução com Espaçamento")
    print("    └─ Adiciona espaço automático entre dados")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Com validação e opções avançadas")
    print()
    print("4️⃣  Comparar todas as soluções")
    print("    └─ Executa todas com os mesmos dados")
    print()
    print("0️⃣  Sair")
    print("-" * 50)


def comparar_solucoes():
    """
    Executa todas as soluções com os mesmos dados para comparação
    """
    print("\n🔄 MODO COMPARAÇÃO")
    print("="*50)
    print("Digite os dados uma vez e veja todas as implementações:")
    print()
    
    # Coletando dados uma única vez
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    print("\n" + "🔍 RESULTADOS DAS DIFERENTES IMPLEMENTAÇÕES:")
    print("="*60)
    
    # Solução 1
    resultado1 = dado1 + dado2
    print(f"1️⃣  Básica:           '{resultado1}'")
    
    # Solução 2
    resultado2 = dado1 + " " + dado2
    print(f"2️⃣  Com espaçamento:  '{resultado2}'")
    
    # Solução 3
    resultado3 = f"{dado1}{dado2}"
    print(f"3️⃣  F-string:         '{resultado3}'")
    
    print("\n📊 ANÁLISE:")
    print(f"   • Dados originais: '{dado1}' + '{dado2}'")
    print(f"   • Tamanho dado 1: {len(dado1)} caracteres")
    print(f"   • Tamanho dado 2: {len(dado2)} caracteres")
    print(f"   • Resultado básico: {len(resultado1)} caracteres")
    print(f"   • Resultado com espaço: {len(resultado2)} caracteres")


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
                solucao_com_espacamento()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                comparar_solucoes()
            elif opcao == "0":
                print("\n👋 Obrigado por usar o Concatenador de Dados!")
                print("🐍 Continue praticando Python! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar
            if opcao in ["1", "2", "3", "4"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar o Concatenador de Dados!")
                    print("🐍 Continue praticando Python! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()