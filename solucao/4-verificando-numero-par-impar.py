"""
Desafio: Verificando Números Pares e Ímpares ��
Múltiplas implementações para verificação de paridade
Autor: Victor Lima e Claude 4 Sonnet
"""

def solucao_basica():
    """
    Versão 1: Implementação básica
    Usando if/else tradicional com operador módulo
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    try:
        # Recebendo o número
        numero = int(input("Digite um número inteiro: "))
        
        # Verificando se é par ou ímpar
        if numero % 2 == 0:
            resultado = "par"
        else:
            resultado = "ímpar"
        
        # Exibindo o resultado
        print(f"O número {numero} é {resultado}.")
        
    except ValueError:
        print("❌ Por favor, digite um número inteiro válido!")


def solucao_otimizada():
    """
    Versão 2: Código otimizado
    Usando operador ternário e validação melhorada
    """
    print("\n🔹 SOLUÇÃO OTIMIZADA")
    print("-" * 30)
    
    try:
        # Recebendo e validando o número
        numero = int(input("Digite um número inteiro: "))
        
        # Verificação otimizada com operador ternário
        resultado = "par" if numero % 2 == 0 else "ímpar"
        
        # Exibindo resultado com mais informações
        print(f"✅ Número: {numero}")
        print(f"📊 Resultado: {resultado}")
        print(f"🔢 Resto da divisão por 2: {numero % 2}")
        
    except ValueError:
        print("❌ Erro: Digite apenas números inteiros!")


def solucao_robusta():
    """
    Versão 3: Implementação robusta e completa
    Com múltiplas validações e análises extras
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    try:
        # Recebendo o número com validação
        while True:
            entrada = input("Digite um número inteiro: ").strip()
            try:
                numero = int(entrada)
                break
            except ValueError:
                print("❌ Entrada inválida! Digite apenas números inteiros.")
        
        # Análise completa do número
        eh_par = numero % 2 == 0
        eh_impar = not eh_par
        
        # Casos especiais
        eh_zero = numero == 0
        eh_positivo = numero > 0
        eh_negativo = numero < 0
        
        # Exibindo análise completa
        print("\n" + "="*50)
        print(f"🔍 ANÁLISE COMPLETA DO NÚMERO {numero}")
        print("="*50)
        
        # Paridade
        paridade = "par" if eh_par else "ímpar"
        print(f"📊 Paridade: {paridade.upper()}")
        
        # Informações extras
        print(f"🔢 Resto da divisão por 2: {numero % 2}")
        print(f"➕ Sinal: {'Zero' if eh_zero else 'Positivo' if eh_positivo else 'Negativo'}")
        print(f"📈 Valor absoluto: {abs(numero)}")
        
        # Análises matemáticas
        print(f"\n🧮 PROPRIEDADES MATEMÁTICAS:")
        print(f"   • É múltiplo de 2: {eh_par}")
        print(f"   • É múltiplo de 3: {numero % 3 == 0}")
        print(f"   • É múltiplo de 5: {numero % 5 == 0}")
        print(f"   • É múltiplo de 10: {numero % 10 == 0}")
        
        # Sequência de números
        print(f"\n📋 SEQUÊNCIA:")
        print(f"   • Anterior: {numero - 1} ({'par' if (numero - 1) % 2 == 0 else 'ímpar'})")
        print(f"   • Atual: {numero} ({paridade})")
        print(f"   • Próximo: {numero + 1} ({'par' if (numero + 1) % 2 == 0 else 'ímpar'})")
        
        print("="*50)
        
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def verificador_multiplo():
    """
    Versão 4: Verificador de múltiplos números
    Permite verificar vários números em sequência
    """
    print("\n🔹 VERIFICADOR MÚLTIPLO")
    print("-" * 30)
    
    numeros_verificados = []
    pares = []
    impares = []
    
    while True:
        try:
            entrada = input("\nDigite um número (ou 'sair' para terminar): ").strip().lower()
            
            if entrada in ['sair', 'exit', 'quit', 's']:
                break
            
            numero = int(entrada)
            numeros_verificados.append(numero)
            
            # Verificando paridade
            if numero % 2 == 0:
                pares.append(numero)
                resultado = "PAR"
                emoji = "✅"
            else:
                impares.append(numero)
                resultado = "ÍMPAR"
                emoji = "🔸"
            
            print(f"{emoji} {numero} é {resultado}")
            
        except ValueError:
            print("❌ Digite um número válido ou 'sair' para terminar!")
        except KeyboardInterrupt:
            print("\n\n👋 Encerrando verificador...")
            break
    
    # Resumo final
    if numeros_verificados:
        print("\n" + "="*60)
        print("📊 RESUMO DA VERIFICAÇÃO")
        print("="*60)
        print(f"🔢 Total de números verificados: {len(numeros_verificados)}")
        print(f"✅ Números pares: {len(pares)} → {pares}")
        print(f"🔸 Números ímpares: {len(impares)} → {impares}")
        
        if pares:
            print(f"📈 Maior par: {max(pares)}")
            print(f"📉 Menor par: {min(pares)}")
        
        if impares:
            print(f"📈 Maior ímpar: {max(impares)}")
            print(f"📉 Menor ímpar: {min(impares)}")
        
        print("="*60)


def metodos_verificacao():
    """
    Versão 5: Diferentes métodos de verificação
    Demonstra várias formas de verificar paridade
    """
    print("\n🔹 MÉTODOS DE VERIFICAÇÃO")
    print("-" * 30)
    
    try:
        numero = int(input("Digite um número para comparar métodos: "))
        
        print(f"\n�� COMPARANDO MÉTODOS PARA O NÚMERO {numero}")
        print("="*60)
        
        # Método 1: Operador módulo
        metodo1 = numero % 2 == 0
        print(f"1️⃣  Módulo (n % 2 == 0): {metodo1}")
        
        # Método 2: Divisão inteira
        metodo2 = numero // 2 * 2 == numero
        print(f"2️⃣  Divisão inteira: {metodo2}")
        
        # Método 3: Operação bit a bit (AND)
        metodo3 = (numero & 1) == 0
        print(f"3️⃣  Operação bit (n & 1 == 0): {metodo3}")
        
        # Método 4: String (último dígito)
        metodo4 = str(numero)[-1] in '02468'
        print(f"4️⃣  Último dígito: {metodo4}")
        
        # Método 5: Função divmod
        _, resto = divmod(numero, 2)
        metodo5 = resto == 0
        print(f"5️⃣  Função divmod: {metodo5}")
        
        # Verificando consistência
        todos_metodos = [metodo1, metodo2, metodo3, metodo4, metodo5]
        consistente = all(m == metodo1 for m in todos_metodos)
        
        print(f"\n✅ Todos os métodos são consistentes: {consistente}")
        resultado_final = "PAR" if metodo1 else "ÍMPAR"
        print(f"🎯 Resultado final: {numero} é {resultado_final}")
        
        # Performance (conceitual)
        print(f"\n⚡ PERFORMANCE (mais rápido → mais lento):")
        print(f"   1. Operação bit (n & 1)")
        print(f"   2. Operador módulo (n % 2)")
        print(f"   3. Divisão inteira")
        print(f"   4. Função divmod")
        print(f"   5. Verificação de string")
        
    except ValueError:
        print("❌ Digite um número válido!")


def jogo_par_impar():
    """
    Versão 6: Jogo interativo de par ou ímpar
    Gamificação do conceito
    """
    print("\n🔹 JOGO PAR OU ÍMPAR")
    print("-" * 30)
    
    pontos = 0
    rodadas = 0
    
    print("🎮 Bem-vindo ao jogo Par ou Ímpar!")
    print("Tente adivinhar se o número é par ou ímpar!")
    
    while True:
        try:
            # Gerando número aleatório ou pedindo entrada
            import random
            
            print(f"\n🎯 RODADA {rodadas + 1}")
            escolha_modo = input("Escolha: (1) Número aleatório (2) Seu número (3) Sair: ").strip()
            
            if escolha_modo == '3':
                break
            elif escolha_modo == '1':
                numero = random.randint(1, 100)
                print(f"🎲 Número sorteado: {numero}")
            elif escolha_modo == '2':
                numero = int(input("Digite seu número: "))
            else:
                print("❌ Opção inválida!")
                continue
            
            # Palpite do usuário
            palpite = input("Seu palpite - (p)ar ou (i)mpar: ").lower().strip()
            
            if palpite not in ['p', 'par', 'i', 'impar']:
                print("❌ Palpite inválido! Use 'p' para par ou 'i' para ímpar.")
                continue
            
            # Verificando resultado
            eh_par = numero % 2 == 0
            palpite_par = palpite in ['p', 'par']
            
            acertou = (eh_par and palpite_par) or (not eh_par and not palpite_par)
            
            resultado_real = "PAR" if eh_par else "ÍMPAR"
            
            if acertou:
                pontos += 1
                print(f"✅ ACERTOU! {numero} é {resultado_real}")
                print(f"🎉 +1 ponto! Total: {pontos}")
            else:
                print(f"❌ ERROU! {numero} é {resultado_real}")
                print(f"😔 Pontos: {pontos}")
            
            rodadas += 1
            
        except ValueError:
            print("❌ Digite um número válido!")
        except KeyboardInterrupt:
            print("\n\n👋 Jogo interrompido!")
            break
    
    # Resultado final
    if rodadas > 0:
        percentual = (pontos / rodadas) * 100
        print(f"\n🏆 RESULTADO FINAL:")
        print(f"   📊 Rodadas: {rodadas}")
        print(f"   ✅ Acertos: {pontos}")
        print(f"   📈 Aproveitamento: {percentual:.1f}%")
        
        if percentual >= 80:
            print("🌟 Excelente! Você domina par e ímpar!")
        elif percentual >= 60:
            print("👍 Bom trabalho!")
        else:
            print("📚 Continue praticando!")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*65)
    print("🧮 VERIFICADOR DE NÚMEROS PARES E ÍMPARES")
    print("="*65)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ If/else tradicional com operador módulo")
    print()
    print("2️⃣  Solução Otimizada")
    print("    └─ Operador ternário e validação melhorada")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Análise completa com propriedades matemáticas")
    print()
    print("4️⃣  Verificador Múltiplo")
    print("    └─ Verifica vários números em sequência")
    print()
    print("5️⃣  Métodos de Verificação")
    print("    └─ Compara diferentes formas de verificar paridade")
    print()
    print("6️⃣  Jogo Par ou Ímpar")
    print("    └─ Versão gamificada e interativa")
    print()
    print("7️⃣  Exemplos e Teoria")
    print("    └─ Conceitos matemáticos e casos especiais")
    print()
    print("0️⃣  Sair")
    print("-" * 65)


def exemplos_e_teoria():
    """
    Demonstra conceitos matemáticos e casos especiais
    """
    print("\n🎯 EXEMPLOS E TEORIA")
    print("="*50)
    
    print("📚 CONCEITOS FUNDAMENTAIS:")
    print("   • Número PAR: divisível por 2 (resto 0)")
    print("   • Número ÍMPAR: não divisível por 2 (resto 1)")
    print("   • Operador módulo (%): retorna o resto da divisão")
    print()
    
    print("🔢 EXEMPLOS PRÁTICOS:")
    exemplos = [0, 1, 2, -3, -4, 100, 101, 1000, 1001]
    
    for num in exemplos:
        resto = num % 2
        tipo = "PAR" if resto == 0 else "ÍMPAR"
        print(f"   {num:4} % 2 = {resto} → {tipo}")
    
    print("\n🧮 PROPRIEDADES MATEMÁTICAS:")
    print("   • Zero é considerado PAR (0 % 2 = 0)")
    print("   • Números negativos seguem a mesma regra")
    print("   • PAR + PAR = PAR")
    print("   • ÍMPAR + ÍMPAR = PAR") 
    print("   • PAR + ÍMPAR = ÍMPAR")
    print("   • PAR × qualquer número = PAR")
    print("   • ÍMPAR × ÍMPAR = ÍMPAR")
    
    print("\n💡 CASOS ESPECIAIS:")
    casos_especiais = [
        (0, "Zero é par por definição matemática"),
        (-2, "Números negativos pares"),
        (-1, "Números negativos ímpares"),
        (2**31, "Números muito grandes"),
        (1, "Menor número ímpar positivo"),
        (2, "Menor número par positivo")
    ]
    
    for num, explicacao in casos_especiais:
        tipo = "PAR" if num % 2 == 0 else "ÍMPAR"
        print(f"   {num}: {tipo} - {explicacao}")
    
    # Teste interativo
    print(f"\n🧪 TESTE SEU CONHECIMENTO:")
    try:
        teste_num = int(input("Digite um número para análise detalhada: "))
        
        eh_par = teste_num % 2 == 0
        tipo = "PAR" if eh_par else "ÍMPAR"
        
        print(f"\n�� ANÁLISE DE {teste_num}:")
        print(f"   • Tipo: {tipo}")
        print(f"   • Cálculo: {teste_num} ÷ 2 = {teste_num // 2} resto {teste_num % 2}")
        print(f"   • Em binário: {bin(teste_num)} (último bit: {'0=par' if eh_par else '1=ímpar'})")
        
        # Sequência
        anterior = teste_num - 1
        proximo = teste_num + 1
        print(f"   • Sequência: {anterior}({('par' if anterior % 2 == 0 else 'ímpar')}) → {teste_num}({tipo.lower()}) → {proximo}({('par' if proximo % 2 == 0 else 'ímpar')})")
        
    except ValueError:
        print("❌ Digite um número válido!")


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
                solucao_otimizada()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                verificador_multiplo()
            elif opcao == "5":
                metodos_verificacao()
            elif opcao == "6":
                jogo_par_impar()
            elif opcao == "7":
                exemplos_e_teoria()
            elif opcao == "0":
                print("\n👋 Obrigado por usar o Verificador!")
                print("🧮 Continue praticando matemática com Python! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar (exceto para verificador múltiplo e jogo)
            if opcao in ["1", "2", "3", "5", "7"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar o Verificador!")
                    print("🧮 Continue praticando matemática com Python! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()