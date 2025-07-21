"""
Desafio: Calculando Média de Notas 📚
Múltiplas implementações para cálculo de médias escolares
Autor: Victor Lima e Claude 4 Sonnet
"""

def solucao_basica():
    """
    Versão 1: Implementação básica
    Calcula média de três notas usando operadores aritméticos
    """
    print("\n🔹 SOLUÇÃO BÁSICA")
    print("-" * 30)
    
    try:
        # Recebendo as três notas
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # Calculando a média usando operadores aritméticos
        media = (nota1 + nota2 + nota3) / 3
        
        # Exibindo o resultado
        print(f"\nNotas: {nota1}, {nota2}, {nota3}")
        print(f"Média: {media:.2f}")
        
    except ValueError:
        print("❌ Por favor, digite notas válidas (números)!")


def solucao_com_validacao():
    """
    Versão 2: Com validação de notas
    Valida se as notas estão no intervalo correto (0-10)
    """
    print("\n🔹 SOLUÇÃO COM VALIDAÇÃO")
    print("-" * 30)
    
    def obter_nota(numero_nota):
        """Função auxiliar para obter uma nota válida"""
        while True:
            try:
                nota = float(input(f"Digite a {numero_nota}ª nota (0-10): "))
                if 0 <= nota <= 10:
                    return nota
                else:
                    print("❌ Nota deve estar entre 0 e 10!")
            except ValueError:
                print("❌ Digite um número válido!")
    
    try:
        # Recebendo as notas com validação
        print("📝 Digite as três notas do aluno:")
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)
        
        # Calculando a média
        soma = nota1 + nota2 + nota3
        media = soma / 3
        
        # Determinando situação do aluno
        if media >= 7.0:
            situacao = "APROVADO ✅"
            emoji = "🎉"
        elif media >= 5.0:
            situacao = "RECUPERAÇÃO ⚠️"
            emoji = "📚"
        else:
            situacao = "REPROVADO ❌"
            emoji = "😔"
        
        # Exibindo resultado detalhado
        print(f"\n{emoji} RESULTADO:")
        print(f"📊 Notas: {nota1} | {nota2} | {nota3}")
        print(f"➕ Soma: {soma}")
        print(f"📈 Média: {media:.2f}")
        print(f"🎯 Situação: {situacao}")
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def solucao_robusta():
    """
    Versão 3: Calculadora de médias robusta
    Múltiplas funcionalidades e análises estatísticas
    """
    print("\n🔹 SOLUÇÃO ROBUSTA")
    print("-" * 30)
    
    def obter_notas():
        """Obtém as notas com validação completa"""
        notas = []
        nomes_notas = ["primeira", "segunda", "terceira"]
        
        for i, nome in enumerate(nomes_notas, 1):
            while True:
                try:
                    nota = float(input(f"Digite a {nome} nota (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("⚠️ Nota deve estar entre 0 e 10!")
                except ValueError:
                    print("❌ Digite um número válido!")
        
        return notas
    
    try:
        # Dados do aluno
        nome_aluno = input("Digite o nome do aluno: ").strip()
        if not nome_aluno:
            nome_aluno = "Aluno"
        
        disciplina = input("Digite a disciplina (opcional): ").strip()
        if not disciplina:
            disciplina = "Disciplina"
        
        print(f"\n📚 Calculando média de {nome_aluno} em {disciplina}")
        print("-" * 50)
        
        # Obtendo notas
        notas = obter_notas()
        nota1, nota2, nota3 = notas
        
        # Cálculos estatísticos
        soma = nota1 + nota2 + nota3
        media = soma / 3
        maior_nota = max(notas)
        menor_nota = min(notas)
        amplitude = maior_nota - menor_nota
        
        # Análise de desempenho
        notas_acima_media = sum(1 for nota in notas if nota > media)
        notas_abaixo_media = sum(1 for nota in notas if nota < media)
        
        # Situação acadêmica
        if media >= 9.0:
            situacao = "EXCELENTE"
            emoji = "🌟"
            cor = "🟢"
        elif media >= 7.0:
            situacao = "APROVADO"
            emoji = "✅"
            cor = "🟢"
        elif media >= 5.0:
            situacao = "RECUPERAÇÃO"
            emoji = "⚠️"
            cor = "🟡"
        else:
            situacao = "REPROVADO"
            emoji = "❌"
            cor = "🔴"
        
        # Pontos necessários para aprovação
        pontos_para_aprovacao = max(0, 21 - soma)  # 21 = 7.0 * 3
        
        # Exibindo relatório completo
        print("\n" + "="*60)
        print(f"📋 RELATÓRIO DE NOTAS - {nome_aluno.upper()}")
        print("="*60)
        print(f"🎓 Disciplina: {disciplina}")
        print(f"📅 Data: {__import__('datetime').datetime.now().strftime('%d/%m/%Y')}")
        print("-"*60)
        
        print(f"📊 NOTAS INDIVIDUAIS:")
        for i, nota in enumerate(notas, 1):
            status = "🔹" if nota == media else "📈" if nota > media else "📉"
            print(f"   {i}ª Nota: {nota:5.1f} {status}")
        
        print(f"\n🧮 CÁLCULOS:")
        print(f"   Soma das notas: {nota1} + {nota2} + {nota3} = {soma}")
        print(f"   Média aritmética: {soma} ÷ 3 = {media:.2f}")
        
        print(f"\n📈 ESTATÍSTICAS:")
        print(f"   Maior nota: {maior_nota}")
        print(f"   Menor nota: {menor_nota}")
        print(f"   Amplitude: {amplitude:.1f}")
        print(f"   Notas acima da média: {notas_acima_media}")
        print(f"   Notas abaixo da média: {notas_abaixo_media}")
        
        print(f"\n{cor} RESULTADO FINAL:")
        print(f"   {emoji} Situação: {situacao}")
        print(f"   📊 Média: {media:.2f}")
        
        if pontos_para_aprovacao > 0 and media < 7.0:
            print(f"   📚 Pontos para aprovação: {pontos_para_aprovacao:.1f}")
            media_necessaria = pontos_para_aprovacao / 3
            print(f"   🎯 Média necessária nas próximas: {media_necessaria:.2f}")
        
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n👋 Cálculo cancelado!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def calculadora_multiplas_notas():
    """
    Versão 4: Calculadora para múltiplas notas
    Permite calcular média de qualquer quantidade de notas
    """
    print("\n🔹 CALCULADORA MÚLTIPLAS NOTAS")
    print("-" * 30)
    
    try:
        # Escolhendo quantidade de notas
        while True:
            try:
                qtd_notas = int(input("Quantas notas deseja calcular (mín. 2)? "))
                if qtd_notas >= 2:
                    break
                else:
                    print("❌ Mínimo de 2 notas!")
            except ValueError:
                print("❌ Digite um número válido!")
        
        # Coletando notas
        notas = []
        soma = 0
        
        print(f"\n📝 Digite {qtd_notas} notas:")
        for i in range(qtd_notas):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        soma += nota  # Usando operador aritmético +=
                        break
                    else:
                        print("⚠️ Nota deve estar entre 0 e 10!")
                except ValueError:
                    print("❌ Digite um número válido!")
        
        # Calculando média usando operadores aritméticos
        media = soma / qtd_notas
        
        # Estatísticas
        maior = max(notas)
        menor = min(notas)
        
        # Exibindo resultado
        print(f"\n📊 RESULTADO:")
        print(f"📋 Notas: {' | '.join(map(str, notas))}")
        print(f"➕ Soma: {soma}")
        print(f"🔢 Quantidade: {qtd_notas}")
        print(f"📈 Média: {soma} ÷ {qtd_notas} = {media:.2f}")
        print(f"⬆️ Maior nota: {maior}")
        print(f"⬇️ Menor nota: {menor}")
        
        # Situação
        if media >= 7.0:
            print(f"✅ Situação: APROVADO (média ≥ 7.0)")
        elif media >= 5.0:
            print(f"⚠️ Situação: RECUPERAÇÃO (5.0 ≤ média < 7.0)")
        else:
            print(f"❌ Situação: REPROVADO (média < 5.0)")
        
    except Exception as e:
        print(f"❌ Erro: {e}")


def comparar_tipos_media():
    """
    Versão 5: Compara diferentes tipos de média
    Demonstra média aritmética, ponderada e harmônica
    """
    print("\n🔹 COMPARAÇÃO DE TIPOS DE MÉDIA")
    print("-" * 30)
    
    try:
        # Coletando notas
        print("Digite as três notas para comparar diferentes médias:")
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))
        nota3 = float(input("Terceira nota: "))
        
        notas = [nota1, nota2, nota3]
        
        # 1. Média Aritmética (tradicional)
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        
        # 2. Média Ponderada (pesos diferentes)
        # Exemplo: 1ª nota peso 2, 2ª nota peso 3, 3ª nota peso 5
        peso1, peso2, peso3 = 2, 3, 5
        soma_ponderada = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
        soma_pesos = peso1 + peso2 + peso3
        media_ponderada = soma_ponderada / soma_pesos
        
        # 3. Média Harmônica
        if all(nota > 0 for nota in notas):
            soma_inversos = (1/nota1) + (1/nota2) + (1/nota3)
            media_harmonica = 3 / soma_inversos
        else:
            media_harmonica = "Indefinida (nota zero)"
        
        # 4. Média Geométrica
        if all(nota > 0 for nota in notas):
            produto = nota1 * nota2 * nota3
            media_geometrica = produto ** (1/3)
        else:
            media_geometrica = "Indefinida (nota zero)"
        
        # Exibindo comparação
        print(f"\n📊 COMPARAÇÃO DE MÉDIAS")
        print("="*50)
        print(f"📋 Notas: {nota1} | {nota2} | {nota3}")
        print("-"*50)
        
        print(f"1️⃣ Média Aritmética:")
        print(f"   Fórmula: (n1 + n2 + n3) ÷ 3")
        print(f"   Cálculo: ({nota1} + {nota2} + {nota3}) ÷ 3")
        print(f"   Resultado: {media_aritmetica:.2f}")
        
        print(f"\n2️⃣ Média Ponderada (pesos: {peso1}, {peso2}, {peso3}):")
        print(f"   Fórmula: (n1×p1 + n2×p2 + n3×p3) ÷ (p1+p2+p3)")
        print(f"   Cálculo: ({nota1}×{peso1} + {nota2}×{peso2} + {nota3}×{peso3}) ÷ {soma_pesos}")
        print(f"   Resultado: {media_ponderada:.2f}")
        
        print(f"\n3️⃣ Média Harmônica:")
        print(f"   Fórmula: n ÷ (1/n1 + 1/n2 + 1/n3)")
        if isinstance(media_harmonica, (int, float)):
            print(f"   Resultado: {media_harmonica:.2f}")
        else:
            print(f"   Resultado: {media_harmonica}")
        
        print(f"\n4️⃣ Média Geométrica:")
        print(f"   Fórmula: ∛(n1 × n2 × n3)")
        if isinstance(media_geometrica, (int, float)):
            print(f"   Resultado: {media_geometrica:.2f}")
        else:
            print(f"   Resultado: {media_geometrica}")
        
        print("="*50)
        
        # Análise
        print(f"\n🔍 ANÁLISE:")
        print(f"   • Média mais comum: Aritmética ({media_aritmetica:.2f})")
        if isinstance(media_ponderada, (int, float)):
            if media_ponderada > media_aritmetica:
                print(f"   • Média ponderada MAIOR que aritmética")
            elif media_ponderada < media_aritmetica:
                print(f"   • Média ponderada MENOR que aritmética")
            else:
                print(f"   • Médias ponderada e aritmética IGUAIS")
        
    except ValueError:
        print("❌ Digite números válidos!")
    except ZeroDivisionError:
        print("❌ Erro de divisão por zero!")
    except Exception as e:
        print(f"❌ Erro: {e}")


def simulador_notas():
    """
    Versão 6: Simulador de cenários de notas
    Ajuda a planejar notas necessárias
    """
    print("\n🔹 SIMULADOR DE CENÁRIOS")
    print("-" * 30)
    
    try:
        print("🎯 Simule cenários para atingir a média desejada!")
        
        # Meta de média
        while True:
            try:
                meta = float(input("Qual média deseja atingir? "))
                if 0 <= meta <= 10:
                    break
                else:
                    print("❌ Meta deve estar entre 0 e 10!")
            except ValueError:
                print("❌ Digite um número válido!")
        
        # Notas já obtidas
        print(f"\nDigite as notas que já possui:")
        nota1 = float(input("Primeira nota (ou 0 se não fez): "))
        nota2 = float(input("Segunda nota (ou 0 se não fez): "))
        
        # Calculando nota necessária na terceira avaliação
        soma_atual = nota1 + nota2
        soma_necessaria = meta * 3
        nota3_necessaria = soma_necessaria - soma_atual
        
        print(f"\n🎯 SIMULAÇÃO PARA MÉDIA {meta}")
        print("="*40)
        print(f"📊 Notas atuais: {nota1} | {nota2} | ?")
        print(f"🧮 Cálculo:")
        print(f"   Meta total: {meta} × 3 = {soma_necessaria}")
        print(f"   Soma atual: {nota1} + {nota2} = {soma_atual}")
        print(f"   Nota necessária: {soma_necessaria} - {soma_atual} = {nota3_necessaria}")
        
        # Análise da viabilidade
        if nota3_necessaria <= 10:
            if nota3_necessaria <= 0:
                print(f"🎉 PARABÉNS! Você já atingiu a meta!")
                print(f"   Média atual: {(nota1 + nota2 + 0) / 3:.2f}")
            else:
                print(f"✅ VIÁVEL: Precisa tirar {nota3_necessaria:.1f} na 3ª nota")
                
                # Cenários
                print(f"\n📋 CENÁRIOS:")
                cenarios = [0, 5, 7, 8.5, 10]
                for cenario in cenarios:
                    if cenario <= 10:
                        media_cenario = (nota1 + nota2 + cenario) / 3
                        status = "✅" if media_cenario >= meta else "❌"
                        print(f"   Se tirar {cenario:4.1f}: média = {media_cenario:.2f} {status}")
        else:
            print(f"❌ IMPOSSÍVEL: Precisaria tirar {nota3_necessaria:.1f}")
            print(f"   (Nota máxima é 10.0)")
            
            # Melhor cenário possível
            melhor_media = (nota1 + nota2 + 10) / 3
            print(f"🎯 Melhor cenário possível: {melhor_media:.2f} (tirando 10)")
        
    except ValueError:
        print("❌ Digite números válidos!")
    except Exception as e:
        print(f"❌ Erro: {e}")


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis
    """
    print("\n" + "="*60)
    print("📚 CALCULADORA DE MÉDIA DE NOTAS")
    print("="*60)
    print("Escolha qual implementação deseja utilizar:")
    print()
    print("1️⃣  Solução Básica")
    print("    └─ Média simples de três notas")
    print()
    print("2️⃣  Solução com Validação")
    print("    └─ Validação de notas e situação acadêmica")
    print()
    print("3️⃣  Solução Robusta")
    print("    └─ Relatório completo com estatísticas")
    print()
    print("4️⃣  Múltiplas Notas")
    print("    └─ Calcular média de qualquer quantidade")
    print()
    print("5️⃣  Tipos de Média")
    print("    └─ Compara diferentes tipos de média")
    print()
    print("6️⃣  Simulador de Cenários")
    print("    └─ Planeje suas notas para atingir metas")
    print()
    print("7️⃣  Exemplos e Conceitos")
    print("    └─ Teoria sobre médias e exemplos práticos")
    print()
    print("0️⃣  Sair")
    print("-" * 60)


def exemplos_e_conceitos():
    """
    Demonstra conceitos sobre médias e exemplos práticos
    """
    print("\n🎯 EXEMPLOS E CONCEITOS")
    print("="*50)
    
    print("📚 CONCEITOS FUNDAMENTAIS:")
    print("   • Média Aritmética: soma dos valores ÷ quantidade")
    print("   • Operadores usados: + (soma) e / (divisão)")
    print("   • Fórmula: (n1 + n2 + n3) ÷ 3")
    print()
    
    print("🔢 EXEMPLOS PRÁTICOS:")
    exemplos = [
        ([8.0, 7.5, 9.0], "Aluno com bom desempenho"),
        ([6.0, 5.5, 8.0], "Aluno em recuperação"),
        ([4.0, 3.5, 5.0], "Aluno reprovado"),
        ([10.0, 10.0, 10.0], "Aluno excelente"),
        ([0.0, 5.0, 10.0], "Desempenho irregular")
    ]
    
    for notas, descricao in exemplos:
        soma = notas[0] + notas[1] + notas[2]  # Usando operador +
        media = soma / 3  # Usando operador /
        
        if media >= 7.0:
            situacao = "APROVADO"
        elif media >= 5.0:
            situacao = "RECUPERAÇÃO"
        else:
            situacao = "REPROVADO"
        
        print(f"\n📝 {descricao}:")
        print(f"   Notas: {notas[0]} | {notas[1]} | {notas[2]}")
        print(f"   Cálculo: ({notas[0]} + {notas[1]} + {notas[2]}) ÷ 3")
        print(f"   Média: {media:.2f} → {situacao}")
    
    print(f"\n🏫 SISTEMA DE AVALIAÇÃO BRASILEIRO:")
    print(f"   • Média ≥ 7.0: APROVADO")
    print(f"   • 5.0 ≤ Média < 7.0: RECUPERAÇÃO")
    print(f"   • Média < 5.0: REPROVADO")
    
    print(f"\n💡 DICAS IMPORTANTES:")
    print(f"   • Sempre valide se as notas estão entre 0 e 10")
    print(f"   • Use float() para aceitar notas decimais")
    print(f"   • Arredonde o resultado para 2 casas decimais")
    print(f"   • Considere diferentes pesos se necessário")
    
    # Calculadora interativa de exemplo
    print(f"\n🧪 TESTE RÁPIDO:")
    try:
        print("Digite três notas para ver o cálculo passo a passo:")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        
        print(f"\n📊 PASSO A PASSO:")
        print(f"   1. Somar as notas: {n1} + {n2} + {n3}")
        soma = n1 + n2 + n3
        print(f"   2. Resultado da soma: {soma}")
        print(f"   3. Dividir por 3: {soma} ÷ 3")
        media = soma / 3
        print(f"   4. Média final: {media:.2f}")
        
    except ValueError:
        print("❌ Digite números válidos!")


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
                solucao_com_validacao()
            elif opcao == "3":
                solucao_robusta()
            elif opcao == "4":
                calculadora_multiplas_notas()
            elif opcao == "5":
                comparar_tipos_media()
            elif opcao == "6":
                simulador_notas()
            elif opcao == "7":
                exemplos_e_conceitos()
            elif opcao == "0":
                print("\n👋 Obrigado por usar a Calculadora de Médias!")
                print("📚 Continue estudando e praticando! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            # Pergunta se quer continuar
            if opcao in ["1", "2", "3", "4", "5", "6", "7"]:
                continuar = input("\nDeseja testar outra solução? (s/n): ").lower().strip()
                if continuar != 's':
                    print("\n👋 Obrigado por usar a Calculadora de Médias!")
                    print("�� Continue estudando e praticando! 🚀")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente...")


if __name__ == "__main__":
    main()