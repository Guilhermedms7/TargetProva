import json

def analise_faturamento(arquivo_json):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            dados = json.load(file)
        
        # Filtra apenas os valores positivos (ignora dias sem faturamento)
        valores = [dia["valor"] for dia in dados if dia["valor"] > 0]

        # Evita erro caso não haja valores válidos no JSON
        if not valores:
            print("Nenhum faturamento registrado.")
            return
        
        # Calcula os resultados
        menor_faturamento = min(valores)
        maior_faturamento = max(valores)
        media_mensal = sum(valores) / len(valores)
        dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

        # Exibe os resultados
        print("3) Faturamento diário:")
        print(f"   Menor valor de faturamento: R$ {menor_faturamento:.2f}")
        print(f"   Maior valor de faturamento: R$ {maior_faturamento:.2f}")
        print(f"   Dias acima da média mensal: {dias_acima_da_media}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{arquivo_json}' não é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função automaticamente
if __name__ == "__main__":
    analise_faturamento("faturamento.json")
