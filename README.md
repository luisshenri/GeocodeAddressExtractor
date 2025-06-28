# GeocodeAddressExtractor
GeocodeAddressExtractor é um sistema desenvolvido em Python que facilita a conversão de coordenadas geográficas (latitude e longitude) em endereços legíveis, utilizando a API do Google Maps. O projeto lê informações de endereços a partir de uma planilha Excel, processa as coordenadas e extrai dados relevantes, como cidade, bairro e CEP, retornando tudo em um arquivo Excel finalizado.

## Funcionalidades Principais:
Leitura de Arquivos Excel: Importa dados de coordenadas geográficas a partir de um arquivo Excel existente.
Correção de Formato de Coordenadas: Converte vírgulas em pontos, garantindo que as coordenadas sejam corretamente reconhecidas como valores numéricos.
Geocodificação Reversa: Utiliza a API do Google Maps para converter coordenadas em endereços legíveis, extraindo informações detalhadas como cidade, bairro e CEP.
Exportação de Resultados: Salva os dados resultantes, incluindo endereços e informações adicionais, em um novo arquivo Excel.
## Pré-requisitos
Python 3.x
KeyApi google
Bibliotecas: pandas, googlemaps, openpyxl
