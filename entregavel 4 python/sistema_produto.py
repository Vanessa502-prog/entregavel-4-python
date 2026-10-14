# 1. CADASTRO DE PRODUTOS
lista_produtos = []

print("=== SISTEMA DE GESTÃO DE PRODUTOS ===")
quantidade_desejada = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_desejada):
    print(f"\nRegisto do Produto {i + 1}:")
    nome_produto = input("  Nome do produto: ")
    preco_produto = float(input("  Preço do produto (R$): "))
    categoria_produto = input("  Categoria do produto: ")
    
    lista_produtos.append({
        "nome": nome_produto,
        "preco": preco_produto,
        "categoria": categoria_produto
    })


# 2. FILTRAGEM POR PREÇO
print("\n--- FILTRAGEM DE PRODUTOS POR PREÇO ---")
preco_limite = float(input("Informe um valor de referência para filtrar: "))
opcao_filtro = input("Deseja listar produtos [A]cima ou [B]baixo deste valor? ").strip().upper()

if opcao_filtro == 'A':
    produtos_filtrados = [p for p in lista_produtos if p["preco"] > preco_limite]
    print(f"\nProdutos com preço ACIMA de R$ {preco_limite:.2f}:")
else:
    produtos_filtrados = [p for p in lista_produtos if p["preco"] < preco_limite]
    print(f"\nProdutos com preço ABAIXO de R$ {preco_limite:.2f}:")

if produtos_filtrados:
    for p in produtos_filtrados:
        print(f" • {p['nome']} ({p['categoria']}) - R$ {p['preco']:.2f}")
else:
    print(" Nenhum produto encontrado com este critério.")


# 3. ORDENAÇÃO (crescente e decrescente)
produtos_crescente = sorted(lista_produtos, key=lambda x: x["preco"])
produtos_decrescente = sorted(lista_produtos, key=lambda x: x["preco"], reverse=True)

print("\n--- ORDENAÇÃO DE PRODUTOS POR PREÇO ---")
print("Preço Crescente (Menor para Maior):")
for p in produtos_crescente:
    print(f" -> {p['nome']}: R$ {p['preco']:.2f}")

print("\nPreço Decrescente (Maior para Menor):")
for p in produtos_decrescente:
    print(f" -> {p['nome']}: R$ {p['preco']:.2f}")


# 4. CONJUNTO DE CATEGORIAS ÚNICAS (set)
categorias_unicas = {p["categoria"] for p in lista_produtos}


# 5. TUPLA DE ESTATÍSTICAS (min, max, média)
if lista_produtos:
    precos_lista = [p["preco"] for p in lista_produtos]
    menor_preco = min(precos_lista)
    maior_preco = max(precos_lista)
    media_precos = sum(precos_lista) / len(precos_lista)
    
    tupla_estatisticas = (menor_preco, maior_preco, media_precos)
else:
    tupla_estatisticas = (0.0, 0.0, 0.0)


# 6. RELATÓRIO FINAL FORMATADO (com f-strings)
print("\n" + "=" * 60)
print(f"{'RELATÓRIO FINAL DO SISTEMA DE PRODUTOS':^60}")
print("=" * 60)
print(f" Total de produtos cadastrados : {len(lista_produtos)}")
print(f" Categorias únicas encontradas : {categorias_unicas}")
print(f" Estatísticas Gerais de Preço:")
print(f"   • Menor Preço Registado     : R$ {tupla_estatisticas[0]:.2f}")
print(f"   • Maior Preço Registado     : R$ {tupla_estatisticas[1]:.2f}")
print(f"   • Média Geral de Preços     : R$ {tupla_estatisticas[2]:.2f}")
print("=" * 60)


#versão em Portugol:
# - Cadastro: Em Portugol, usa-se vetores fixos (ex: cadeia nomes[50]) com um 
#   contador de controle e laços "para" para a leitura via teclado.
# - Filtragem: Percorre-se o vetor estático com um laço e usa-se uma estrutura 
#   condicional "se" para exibir apenas os valores desejados.
# - Ordenação: Sem funções prontas como sorted(), implementa-se o algoritmo 
#   Bubble Sort (Método da Bolha) com laços duplos e variáveis auxiliares de troca.
# - Conjuntos: A eliminação de duplicatas (set) é simulada comparando manualmente 
#   cada nova categoria com as já armazenadas em um vetor exclusivo.
# - Estatísticas: Inicializa-se com o primeiro valor e percorre-se o vetor 
#   atualizando os menores/maiores valores e acumulando a soma para tirar a média.