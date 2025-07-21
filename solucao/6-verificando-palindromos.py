"""
Desafio: Verificando Palíndromos 🔄
Múltiplas implementações para verificação de palíndromos
Autor: Victor Lima e Claude 4 Sonnet
"""

def solucao_basica():
    """
    Versão 1: Implementação básica
    Inverte string usando slicing e compara com original
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    # Recebendo a palavra
    palavra = input("Digite uma palavra: ").strip()
    
    # Invertendo a string usando slicing
    palavra_invertida = palavra[::-1]
    
    # Comparando original com invertida
    if palavra == palavra_invertida:
        resultado = "é um palíndromo"
        emoji = "✅"
    else:
        resultado = "não é um palíndromo"
        emoji = "❌"
    
    # Exibindo o resultado
    print(f"\nPalavra original: '{palavra}'")
    print(f"Palavra invertida: '{palavra_invertida}'")
    print(f"{emoji} A palavra '{palavra}' {resultado}!")


def solucao_case_insensitive():
    """
    Versão 2: Ignora maiúsculas/minúsculas
    Trata diferenças de case para verificação mais robusta
    """
    print("\n🔹 SOLUÇÃO CASE-INSENSITIVE")
    print("-" * 30)
    
    # Recebendo a palavra
    palavra_original = input("Digite uma palavra: ").strip()
    
    # Convertendo para minúsculas para comparação
    palavra = palavra_original.lower()
    
    # Invertendo a string
    palavra_invertida = palavra[::-1]
    
    # Verificando se é palíndromo
    eh_palindromo = palavra == palavra_invertida
    
    # Exibindo resultado detalhado
    print(f"\n📝 Análise:")
    print(f"   Palavra original: '{palavra_original}'")
    print(f"   Normalizada: '{palavra}'")
    print(f"   Invertida: '{palavra_invertida}'")
    print(f"   Comparação: '{palavra}' == '{palavra_invertida}' → {eh_palindromo}")
    
    if eh_palindromo:
        print(f"✅ '{palavra_original}' É UM PALÍNDROMO! ��")
    else:
        print(f"❌ '{palavra_original}' NÃO é um palíndromo.")


def solucao_robusta():
    """
    Versão 3: Implementação robusta
    Remove espaços, pontuação e trata caracteres especiais
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    import re
    
    # Recebendo o texto
    texto_original = input("Digite uma palavra ou frase: ").strip()
    
    if not texto_original:
        print("❌ Texto não pode estar vazio!")
        return
    
    # Normalizando o texto (removendo espaços, pontuação, acentos)
    # Mantendo apenas letras e números, convertendo para minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto_original.lower())
    
    # Tratando acentos (versão simplificada)
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c'
    }
    
    for acento, letra in acentos.items():
        texto_limpo = texto_limpo.replace(acento, letra)
    
    # Invertendo o texto limpo
    texto_invertido = texto_limpo[::-1]
    
    # Verificando se é palíndromo
    eh_palindromo = texto_limpo == texto_invertido
    
    # Análise detalhada
    print(f"\n🔍 ANÁLISE DETALHADA:")
    print("="*50)
    print(f"📝 Texto original: '{texto_original}'")
    print(f"🧹 Texto limpo: '{texto_limpo}'")
    print(f"🔄 Texto invertido: '{texto_invertido}'")
    print(f"📊 Tamanho: {len(texto_limpo)} caracteres")
    print("-"*50)
    
    if eh_palindromo:
        print(f"✅ É UM PALÍNDROMO! 🎉")
        print(f"🎯 '{texto_original}' lê-se igual de frente para trás!")
    else:
        print(f"❌ NÃO é um palíndromo.")
        
        # Mostrando diferenças
        print(f"\n🔍 Diferenças encontradas:")
        for i, (char1, char2) in enumerate(zip(texto_limpo, texto_invertido)):
            if char1 != char2:
                print(f"   Posição {i}: '{char1}' ≠ '{char2}'")
                break
    
    print("="*50)


def metodos_inversao():
    """
    Versão 4: Diferentes métodos de inversão
    Demonstra várias formas de inverter strings
    """
    print("\n🔹 MÉTODOS DE INVERSÃO")
    print("-" * 30)
    
    # Recebendo a palavra
    palavra = input("Digite uma palavra para comparar métodos: ").strip().lower()
    
    print(f"\n🔄 COMPARANDO MÉTODOS DE INVERSÃO PARA: '{palavra}'")
    print("="*60)
    
    # Método 1: Slicing (mais comum)
    metodo1 = palavra[::-1]
    print(f"1️⃣  Slicing ([::-1]): '{metodo1}'")
    
    # Método 2: Função reversed() + join()
    metodo2 = ''.join(reversed(palavra))
    print(f"2️⃣  Reversed + join: '{metodo2}'")
    
    # Método 3: Loop manual
    metodo3 = ""
    for char in palavra:
        metodo3 = char + metodo3
    print(f"3️⃣  Loop manual: '{metodo3}'")
    
    # Método 4: Recursão
    def inverter_recursivo(s):
        if len(s) <= 1:
            return s
        return s[-1] + inverter_recursivo(s[:-1])
    
    metodo4 = inverter_recursivo(palavra)
    print(f"4️⃣  Recursão: '{metodo4}'")
    
    # Método 5: List comprehension
    metodo5 = ''.join([palavra[i] for i in range(len(palavra)-1, -1, -1)])
    print(f"5️⃣  List comprehension: '{metodo5}'")
    
    # Verificando consistência
    todos_metodos = [metodo1, metodo2, metodo3, metodo4, metodo5]
    consistente = all(m == metodo1 for m in todos_metodos)
    
    print(f"\n✅ Todos os métodos são consistentes: {consistente}")
    
    # Verificando se é palíndromo
    eh_palindromo = palavra == metodo1
    print(f"🎯 '{palavra}' é palíndromo: {eh_palindromo}")
    
    # Performance (conceitual)
    print(f"\n⚡ PERFORMANCE (mais rápido → mais lento):")
    print(f"   1. Slicing [::-1] - Mais eficiente")
    print(f"   2. Reversed + join")
    print(f"   3. List comprehension")
    print(f"   4. Loop manual")
    print(f"   5. Recursão - Menos eficiente para strings grandes")


def verificador_multiplo():
    """
    Versão 5: Verificador de múltiplas palavras
    Permite testar várias palavras em sequência
    """
    print("\n🔹 VERIFICADOR MÚLTIPLO")
    print("-" * 30)
    
    palindromos_encontrados = []
    nao_palindromos = []
    total_testados = 0
    
    print("🔄 Digite palavras para verificar (digite 'sair' para terminar)")
    
    while True:
        entrada = input(f"\nPalavra {total_testados + 1}: ").strip()
        
        if entrada.lower() in ['sair', 'exit', 'quit', 's']:
            break
        
        if not entrada:
            print("❌ Digite uma palavra válida!")
            continue
        
        # Normalizando
        palavra_limpa = entrada.lower()
        palavra_invertida = palavra_limpa[::-1]
        
        # Verificando
        eh_palindromo = palavra_limpa == palavra_invertida
        total_testados += 1
        
        if eh_palindromo:
            palindromos_encontrados.append(entrada)
            print(f"✅ '{entrada}' É palíndromo!")
        else:
            nao_palindromos.append(entrada)
            print(f"❌ '{entrada}' NÃO é palíndromo")
    
    # Relatório final
    if total_testados > 0:
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL")
        print("="*60)
        print(f"🔢 Total testado: {total_testados} palavras")
        print(f"✅ Palíndromos: {len(palindromos_encontrados)}")
        print(f"❌ Não palíndromos: {len(nao_palindromos)}")
        
        if palindromos_encontrados:
            print(f"\n🎉 PALÍNDROMOS ENCONTRADOS:")
            for i, palindromo in enumerate(palindromos_encontrados, 1):
                print(f"   {i}. {palindromo}")
        
        if nao_palindromos:
            print(f"\n📝 NÃO PALÍNDROMOS:")
            for i, nao_palindromo in enumerate(nao_palindromos, 1):
                print(f"   {i}. {nao_palindromo}")
        
        # Estatísticas
        percentual_palindromos = (len(palindromos_encontrados) / total_testados) * 100
        print(f"\n📈 {percentual_palindromos:.1f}% das palavras testadas são palíndromos")
        print("="*60)


def jogo_palindromos():
    """
    Versão 6: Jogo de adivinhação de palíndromos
    Gamificação do conceito
    """
    print("\n🔹 JOGO DOS PALÍNDROMOS")
    print("-" * 30)
    
    import random
    
    # Lista de palavras para o jogo
    palavras_teste = [
        # Palíndromos
        ("arara", True), ("ovo", True), ("osso", True), ("radar", True),
        ("level", True), ("civic", True), ("kayak", True), ("madam", True),
        ("racecar", True), ("rotator", True),
        # Não palíndromos
        ("python", False), ("casa", False), ("computador", False),
        ("programacao", False), ("algoritmo", False), ("dados", False),
        ("string", False), ("codigo", False), ("funcao", False), ("loop", False)
    ]
    
    pontos = 0
    rodadas = 0
    
    print("🎮 Bem-vindo ao Jogo dos Palíndromos!")
    print("Tente adivinhar se a palavra é um palíndromo!")
    
    while True:
        # Escolhendo palavra aleatória
        palavra, eh_palindromo_real = random.choice(palavras_teste)
        rodadas += 1
        
        print(f"\n🎯 RODADA {rodadas}")
        print(f"📝 Palavra: '{palavra.upper()}'")
        
        # Palpite do usuário
        while True:
            palpite = input("É palíndromo? (s/n) ou 'sair': ").lower().strip()
            if palpite in ['s', 'sim', 'n', 'nao', 'não', 'sair']:
                break
            print("❌ Digite 's' para sim, 'n' para não, ou 'sair'")
        
        if palpite == 'sair':
            break
        
        # Verificando resposta
        palpite_eh_palindromo = palpite in ['s', 'sim']
        
        # Mostrando a verificação real
        palavra_invertida = palavra[::-1]
        print(f"\n🔍 Verificação:")
        print(f"   Original: '{palavra}'")
        print(f"   Invertida: '{palavra_invertida}'")
        print(f"   É palíndromo: {eh_palindromo_real}")
        
        # Verificando acerto
        if palpite_eh_palindromo == eh_palindromo_real:
            pontos += 1
            print(f"✅ ACERTOU! +1 ponto")
        else:
            print(f"❌ ERROU!")
        
        print(f"🏆 Pontuação: {pontos}/{rodadas}")
        
        # Continuar?
        continuar = input("\nPróxima palavra? (s/n): ").lower().strip()
        if continuar not in ['s', 'sim']:
            break
    
    # Resultado final
    if rodadas > 0:
        percentual = (pontos / rodadas) * 100
        print(f"\n🏆 RESULTADO FINAL:")
        print(f"   📊 Rodadas: {rodadas}")
        print(f"   ✅ Acertos: {pontos}")
        print(f"   📈 Aproveitamento: {percentual:.1f}%")
        
        if percentual >= 80:
            print("🌟 Excelente! Você é um expert em palíndromos!")
        elif percentual >= 60:
            print("👍 Bom trabalho! Continue praticando!")
        else:
            print("📚 Continue estudando palíndromos!")


def exemplos_e_teoria():
    """
    Demonstra conceitos e exemplos de palíndromos
    """
    print("\n🎯 EXEMPLOS E TEORIA")
    print("="*50)
    
    print("📚 CONCEITO DE PALÍNDROMO:")
    print("   • Palavra que se lê igual de frente para trás")
    print("   • Exemplo: 'ARARA' → A-R-A-R-A")
    print("   • Invertido: A-R-A-R-A (igual!)")
    print()
    
    print("🔤 EXEMPLOS EM PORTUGUÊS:")
    palindromos_pt = [
        "arara", "ovo", "osso", "radar", "reviver", "socos",
        "ana", "asa", "ele", "eme", "oro", "rir"
    ]
    
    for palavra in palindromos_pt:
        invertida = palavra[::-1]
        print(f"   '{palavra}' → '{invertida}' ✅")
    
    print(f"\n🌍 EXEMPLOS EM INGLÊS:")
    palindromos_en = [
        "level", "civic", "kayak", "madam", "racecar", "rotator",
        "noon", "deed", "peep", "mom", "dad", "wow"
    ]
    
    for palavra in palindromos_en:
        invertida = palavra[::-1]
        print(f"   '{palavra}' → '{invertida}' ✅")
    
    print(f"\n🔢 PALÍNDROMOS NUMÉRICOS:")
    numeros_palindromos = ["121", "1331", "12321", "123454321"]
    
    for numero in numeros_palindromos:
        invertido = numero[::-1]
        print(f"   {numero} → {invertido} ✅")
    
    print(f"\n📝 FRASES PALÍNDROMAS (sem espaços):")
    frases = [
        ("A cara rajada da jararaca", "acarajadadajararaca"),
        ("Socorram me subi no onibus em marrocos", "socorrammesubinoonibusemmarrocos"),
        ("A mala nada na lama", "amalanadalama")
    ]
    
    for frase_original, frase_limpa in frases:
        invertida = frase_limpa[::-1]
        eh_palindromo = frase_limpa == invertida
        print(f"   '{frase_original}'")
        print(f"   Limpa: '{frase_limpa}' → {eh_palindromo} ✅")
        print()
    
    # Teste interativo
    print(f"🧪 TESTE SEU PRÓPRIO EXEMPLO:")
    try:
        teste = input("Digite uma palavra para verificar: ").strip().lower()
        if teste:
            invertida = teste[::-1]
            eh_palindromo = teste == invertida
            
            print(f"\n📊 ANÁLISE:")
            print(f"   Original: '{teste}'")
            print(f"   Invertida: '{invertida}'")
            print(f"   É palíndromo: {eh_palindromo}")
            
            if eh_palindromo:
                print(f"   🎉 PARABÉNS! Você encontrou um palíndromo!")
            else:
                print(f"   �� Não é palíndromo, mas continue tentando!")
    
    except Exception as e:
        print(f"❌ Erro: {e}")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*60)
    print("🔄 VERIFICADOR DE PALÍNDROMOS")
    print("="*60)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ Inversão simples com slicing e comparação")
    print()
    print("2️⃣  Solução Case-Insensitive")
    print("    └─ Ignora maiúsculas e minúsculas")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Remove espaços, pontuação e acentos")
    print()
    print("4️⃣  Métodos de Inversão")
    print("    └─ Compara diferentes formas de inverter strings")
    print()
    print("5️⃣  Verificador Múltiplo")
    print("    └─ Testa várias palavras em sequência")
    print()
    print("6️⃣  Jogo dos Palíndromos")
    print("    └─ Versão gamificada e interativa")
    print()
    print("7️⃣  Exemplos e Teoria")
    print("    └─ Conceitos e exemplos práticos")
    print()
    print("0️⃣  Sair")
    print("-" * 60)


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
                solucao_case_insensitive()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                metodos_inversao()
            elif opcao == "5":
                verificador_multiplo()
            elif opcao == "6":
                jogo_palindromos()
            elif opcao == "7":
                exemplos_e_teoria()
            elif opcao == "0":
                print("\n👋 Obrigado por usar o Verificador de Palíndromos!")
                print("🔄 Continue praticando manipulação de strings! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar (exceto para verificador múltiplo e jogo)
            if opcao in ["1", "2", "3", "4", "7"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar o Verificador de Palíndromos!")
                    print("🔄 Continue praticando manipulação de strings! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()