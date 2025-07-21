"""
Desafio: Repetindo Textos ✏️
Múltiplas implementações para repetição de strings
Autor: Victor Lima e Claude 4 Sonnet
"""

def solucao_basica():
    """
    Versão 1: Implementação básica
    Repetição simples usando operador *
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    # Recebendo os dados do usuário
    texto = input("Digite o texto a ser repetido: ")
    numero = int(input("Digite quantas vezes repetir: "))
    
    # Repetindo o texto
    resultado = texto * numero
    
    # Exibindo o resultado
    print("Resultado:", resultado)


def solucao_com_separador():
    """
    Versão 2: Com separador entre repetições
    Adiciona separador personalizado entre as repetições
    """
    print("\n🔹 SOLUÇÃO COM SEPARADOR")
    print("-" * 30)
    
    # Recebendo os dados do usuário
    texto = input("Digite o texto a ser repetido: ")
    numero = int(input("Digite quantas vezes repetir: "))
    separador = input("Digite o separador (ou pressione Enter para nenhum): ")
    
    # Repetindo com separador
    if separador:
        resultado = separador.join([texto] * numero)
    else:
        resultado = texto * numero
    
    # Exibindo o resultado
    print(f"Resultado: {resultado}")


def solucao_robusta():
    """
    Versão 3: Implementação robusta
    Com validação, múltiplas opções e tratamento de erros
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    try:
        # Recebendo e validando o texto
        texto = input("Digite o texto a ser repetido: ").strip()
        if not texto:
            print("⚠️ Texto não pode estar vazio!")
            return
        
        # Recebendo e validando o número
        while True:
            try:
                numero = int(input("Digite quantas vezes repetir (número positivo): "))
                if numero < 0:
                    print("❌ Por favor, digite um número positivo!")
                    continue
                elif numero == 0:
                    print("⚠️ Resultado será uma string vazia!")
                break
            except ValueError:
                print("❌ Por favor, digite um número válido!")
        
        # Opções de formatação
        print("\n📋 Opções de formatação:")
        print("1. Repetição simples (sem separador)")
        print("2. Com separador personalizado")
        print("3. Em linhas separadas")
        print("4. Numerado")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        # Processando baseado na opção
        if opcao == "1":
            resultado = texto * numero
        
        elif opcao == "2":
            separador = input("Digite o separador: ")
            resultado = separador.join([texto] * numero)
        
        elif opcao == "3":
            resultado = "\n".join([texto] * numero)
        
        elif opcao == "4":
            resultado = "\n".join([f"{i+1}. {texto}" for i in range(numero)])
        
        else:
            print("⚠️ Opção inválida, usando repetição simples...")
            resultado = texto * numero
        
        # Exibindo resultados detalhados
        print("\n" + "="*50)
        print(f"📝 Texto original: '{texto}' ({len(texto)} chars)")
        print(f"🔢 Repetições: {numero}")
        print(f"📊 Tamanho final: {len(resultado)} caracteres")
        print("="*50)
        print("✅ RESULTADO:")
        print(resultado)
        print("="*50)
        
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def solucao_com_loop():
    """
    Versão 4: Usando loop for (alternativa ao operador *)
    Demonstra implementação manual da repetição
    """
    print("\n🔹 SOLUÇÃO COM LOOP")
    print("-" * 30)
    
    try:
        # Recebendo os dados
        texto = input("Digite o texto a ser repetido: ")
        numero = int(input("Digite quantas vezes repetir: "))
        
        # Repetindo usando loop
        resultado = ""
        for i in range(numero):
            resultado += texto
        
        # Exibindo o resultado
        print(f"Resultado (usando loop): {resultado}")
        print(f"Iterações realizadas: {numero}")
        
    except ValueError:
        print("❌ Por favor, digite um número válido!")
    except Exception as e:
        print(f"❌ Erro: {e}")


def comparar_metodos():
    """
    Compara diferentes métodos de repetição
    """
    print("\n🔄 COMPARAÇÃO DE MÉTODOS")
    print("="*50)
    
    # Coletando dados uma única vez
    texto = input("Digite o texto para comparar métodos: ")
    try:
        numero = int(input("Digite quantas vezes repetir: "))
    except ValueError:
        print("❌ Número inválido!")
        return
    
    print(f"\n🔍 COMPARANDO MÉTODOS COM: '{texto}' x {numero}")
    print("="*60)
    
    # Método 1: Operador *
    resultado1 = texto * numero
    print(f"1️⃣  Operador *:        '{resultado1[:50]}{'...' if len(resultado1) > 50 else ''}'")
    
    # Método 2: Join
    resultado2 = "".join([texto] * numero)
    print(f"2️⃣  Join:              '{resultado2[:50]}{'...' if len(resultado2) > 50 else ''}'")
    
    # Método 3: Loop
    resultado3 = ""
    for i in range(numero):
        resultado3 += texto
    print(f"3️⃣  Loop:              '{resultado3[:50]}{'...' if len(resultado3) > 50 else ''}'")
    
    # Método 4: List comprehension
    resultado4 = "".join([texto for _ in range(numero)])
    print(f"4️⃣  List comprehension: '{resultado4[:50]}{'...' if len(resultado4) > 50 else ''}'")
    
    # Verificando se todos são iguais
    todos_iguais = resultado1 == resultado2 == resultado3 == resultado4
    print(f"\n✅ Todos os métodos produzem o mesmo resultado: {todos_iguais}")
    print(f"📊 Tamanho do resultado: {len(resultado1)} caracteres")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*55)
    print("✏️ REPETIDOR DE TEXTOS - MÚLTIPLAS IMPLEMENTAÇÕES")
    print("="*55)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ Repetição simples com operador *")
    print()
    print("2️⃣  Solução com Separador")
    print("    └─ Adiciona separador entre repetições")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Validação e múltiplas opções de formatação")
    print()
    print("4️⃣  Solução com Loop")
    print("    └─ Implementação manual usando for")
    print()
    print("5️⃣  Comparar Métodos")
    print("    └─ Testa diferentes formas de repetição")
    print()
    print("6️⃣  Exemplos Práticos")
    print("    └─ Casos de uso interessantes")
    print()
    print("0️⃣  Sair")
    print("-" * 55)


def exemplos_praticos():
    """
    Demonstra casos de uso práticos e interessantes
    """
    print("\n🎯 EXEMPLOS PRÁTICOS")
    print("="*50)
    
    exemplos = [
        ("🌟", 10, "Criando uma linha de estrelas"),
        ("Python ", 3, "Repetindo palavras"),
        ("=", 30, "Criando separadores"),
        ("🎵", 5, "Padrão musical"),
        ("01", 8, "Padrão binário"),
        ("-= ", 15, "Efeito visual")
    ]
    
    for texto, repeticoes, descricao in exemplos:
        resultado = texto * repeticoes
        print(f"📝 {descricao}:")
        print(f"   Entrada: '{texto}' x {repeticoes}")
        print(f"   Resultado: {resultado}")
        print()
    
    # Exemplo interativo
    print("🎮 TESTE VOCÊ MESMO:")
    try:
        texto_user = input("Digite um texto para o exemplo: ")
        num_user = int(input("Quantas repetições: "))
        resultado_user = texto_user * num_user
        print(f"✨ Seu resultado: {resultado_user}")
    except ValueError:
        print("❌ Número inválido!")


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
                solucao_com_separador()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                solucao_com_loop()
            elif opcao == "5":
                comparar_metodos()
            elif opcao == "6":
                exemplos_praticos()
            elif opcao == "0":
                print("\n👋 Obrigado por usar o Repetidor de Textos!")
                print("✏️ Continue praticando Python! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar
            if opcao in ["1", "2", "3", "4", "5", "6"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar o Repetidor de Textos!")
                    print("✏️ Continue praticando Python! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()