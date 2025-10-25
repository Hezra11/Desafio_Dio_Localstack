#Código de estrutura básica do lambda
import json

def lambda_handler(event, context):
    # Seu código aqui
    print("Evento recebido:", json.dumps(event))
    # Exemplo de retorno
    return {
        'statusCode': 200,
        'body': json.dumps('Olá, Lambda!')
    }