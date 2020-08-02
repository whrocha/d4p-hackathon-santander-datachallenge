# d4p-hackathon-santander-datachallenge
Hackathon Santander Data Challenge

## ETL (Crawler Twitter)

O arquivo `tweets_extracts.py` contém o codigo desenvolvido para realizar a busca os tweets utilizados para direcionar os leads.

## Análise

O notebook `hackathon-data-challenge.ipynb` contém a análise dos tweets e o direcionamento dos leads para o empreendedor.

## Banco de dados tweets

O arquivo `hackathon-santander-twitter-db` contem os tweets coletados ate o dia 02-Ago-2020 19h30 UTC-3

## Arquitetura da solução

![Alt text](img/arquiterura_solucao.jpg?raw=true "Title")

O crawler desenvolvido fica pesquisa através do stream da biblioteca pymongo, onde os dados são extraídos de forma live, ou seja, um tweet é feito o crawler já captura esse tweet, o tweet capturado é enviado para o MongoDB gerenciado pelo serviço Atlas, uma soluçao altamente escalável da própria fabricante.

A análise de sentimento é realizada atráves do IBM Watson Sentiment Analysis, mais detalhes desse serviço pode ser encontrato [IBM Watson](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#sentiment).
