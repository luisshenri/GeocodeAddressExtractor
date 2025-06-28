import pandas as pd
import googlemaps

lista_end = "Enderecos_Links.xlsx"
coluna_latitude = "LATITUDE"
coluna_longitude = "LONGITUDE"
coluna_endereco = "ENDEREÇO"
arquivo_resultado = "LINKS408.xlsx"
gmaps = googlemaps.Client(key='xxxxxxxxxxxxxxxxxxxx')


# === LEITURA DA PLANILHA ===
try:
    df = pd.read_excel(lista_end)
except Exception as e:
    print(f"Erro ao carregar o arquivo Excel: {e}")
    exit()
print("Arquivo carregado com sucesso.")

# === CORRIGE VÍRGULAS NAS COORDENADAS ===
try:
    df[coluna_latitude] = df[coluna_latitude].astype(str).str.replace(',', '.').astype(float)
    df[coluna_longitude] = df[coluna_longitude].astype(str).str.replace(',', '.').astype(float)
except Exception as e:
    print(f"Erro ao converter latitude/longitude para float: {e}")
    exit()

# === ADICIONA COLUNAS SE NECESSÁRIO ===
for coluna in ["CIDADE", "BAIRRO", "CEP"]:
    if coluna not in df.columns:
        df[coluna] = ""

# === PROCESSAMENTO DAS COORDENADAS ===
for i, row in df.iterrows():
    lat = row[coluna_latitude]
    lng = row[coluna_longitude]

    try:
        resultado = gmaps.reverse_geocode((lat, lng))
        if resultado:
            endereco_formatado = resultado[0].get("formatted_address", "")
            componentes = resultado[0].get("address_components", [])
            cidade = ""
            bairro = ""
            cep = ""
            for comp in componentes:
                tipos = comp.get("types", [])
                if "locality" in tipos or "administrative_area_level_2" in tipos:
                    cidade = comp["long_name"]
                if "sublocality" in tipos or "neighborhood" in tipos:
                    bairro = comp["long_name"]
                if "postal_code" in tipos:
                    cep = comp["long_name"]

            # Preenche os dados no DataFrame
            df.at[i, coluna_endereco] = endereco_formatado
            df.at[i, "CIDADE"] = cidade
            df.at[i, "BAIRRO"] = bairro
            df.at[i, "CEP"] = cep
    except Exception as e:
        print(f"Erro na linha {i}: {e}")

# === SALVA O ARQUIVO FINAL ===
try:
    df.to_excel(arquivo_resultado, index=False)
    print(f"Arquivo salvo com sucesso como: {arquivo_resultado}")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
