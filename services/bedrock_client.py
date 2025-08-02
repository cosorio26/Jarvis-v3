# Importamos las librerías necesarias
import json
import os
import boto3

# Funcion para invocar a Bedrock
def invoke_bedrock(prompt):

    # Instanciamos el agente
    cliente = boto3.client(
        service_name="bedrock-agent-runtime",
        region_name="us-east-1"
    )

    # Definimos el cuerpo de la solicitud
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {
                "role": "user",
                "content": f"Humano: {prompt} \nAsistente:"
            }
        ],
        "max_tokens": 300
    }

    # Invocamos el agente Jarvis con los parámetros necesarios
    response = cliente.invoke_agent(
        agentId=os.getenv("BEDROCK_AGENT_ID"),
        agentAliasId=os.getenv("BEDROCK_AGENT_ALIAS"),
        sessionId="JarvisSession",
        endSession=False,
        inputText=json.dumps(body)
    )

    # Ciclo para manejar la respuesta del modelo
    full_response = ""
    for event in response['completion']:
        if 'chunk' in event:
            full_response += event['chunk']['bytes'].decode('utf-8')
    
    # Retornamos la respuesta completa del modelo
    return full_response