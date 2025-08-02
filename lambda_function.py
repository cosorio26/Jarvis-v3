# Importamos las librerias necesarias
import json
import time
import random
from handlers.telegram_handler import extract_message
from services.bedrock_client import invoke_bedrock
from services.telegram_client import send_message_to_telegram


# Funcion que recibe los eventos 
def lambda_handler(event, context):

    # Controlamos la excepcion de eventos
    try:
        # Extraemos chatid y mensaje del evento
        chat_id, message_text = extract_message(event)

        # Invocamos a Bedrock con el mensaje recibido
        try:
            response = invoke_bedrock(message_text)
        except ThrottlingException:
            delay = random.uniform(1.5, 3.0) # Esperamos un tiempo aleatorio entre 1.5 y 3 segundos
            print(f"Throttling detectado, esperando {delay} segundos antes de reintentar...")
            time.sleep(delay)
            # Reintentamos invocar a Bedrock
            response = invoke_bedrock(message_text)
                                      
        # Enviamos la respuesta a Telegram
        send_message_to_telegram(chat_id, response)

        # Retornamos la respuesta
        return {
            "statusCode": 200,
            "body": json.dumps("Mensaje procesado y enviado a Telegram con respuesta de Bedrock")
        }

    except Exception as e:
        # Imprimimos el error
        print(f"Error en ejecución Lambda: {e}")
        # Retornamos un mensaje de error
        return {
            "statusCode": 500,
            "body": json.dumps("Error procesando el mensaje")
        }