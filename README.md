# d4p-hackathon-santander-datachallenge
Hackathon Santander Data Challenge organizado pela [Shawee](https://shawee.io/) em 01/Ago/2020 - 02/Ago/2020.

## ETL (Crawler Twitter)

O arquivo `tweets_extracts.py` contém o codigo desenvolvido para realizar a busca dos tweets utilizados para direcionar os leads.

## Análise

O notebook `hackathon-data-challenge.ipynb` contém a análise dos tweets e o direcionamento dos leads para o empreendedor.

## Banco de dados tweets

O arquivo `hackathon-santander-twitter-db` contém os tweets coletados até o dia 02-Ago-2020 19h30 UTC-3

## Arquitetura da solução

![Alt text](img/arquiterura_solucao.jpg?raw=true "Title")

O crawler desenvolvido fica pesquisando através do stream da biblioteca [pymongo](https://pymongo.readthedocs.io/en/stable/), onde os dados são extraídos de forma live, ou seja, um tweet é feito o crawler já captura esse tweet, o tweet capturado é então enviado para o MongoDB gerenciado pelo serviço [Atlas](https://www.mongodb.com/cloud/atlas), uma soluçao altamente escalável da própria fabricante da base de dados.

A análise de sentimento é realizada atráves do IBM Watson Sentiment Analysis, mais detalhes desse serviço pode ser encontrado em [IBM Watson](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#sentiment).
