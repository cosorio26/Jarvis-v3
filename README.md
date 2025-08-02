# 🤖 Telegram → Bedrock Agent | AWS Lambda

Proyecto E2E para integrar flujos conversacionales entre usuarios de Telegram y agentes de IA generativa (Bedrock Agents), desplegado serverless sobre AWS Lambda. Diseñado con arquitectura limpia, trazabilidad y CI/CD automatizado.

---

## 📦 Estructura del Proyecto

```bash
telegram-bedrock-lambda/
│
├── lambda_function.py             # Entry point AWS Lambda
├── handlers/
│   └── telegram_handler.py        # Extrae información de los eventos
├── services/
│   ├── bedrock_client.py          # Conecta con Bedrock
│   └── telegram_client.py         # Envía mensaje a Telagram
├── requirements.txt               # Dependencias si usas layers o testing local
├── README.md                      # Documentación del proyecto
├── .github/
│   └── workflows/
│       └── deploy.yml             # Workflow para despliegue automatizado

```

## Flujo
  1. Usuario envía un mensaje por Telegram
  2. Webhook lo recibe vía API Gateway -> Lambda
  3. Lambda_funtion -> Recibe el evento y orquesta
  4. Extrae la información necesaria por medio de telegram_handler (chat_id - mensaje)
  5. Invoca el agente Bedrock por medio de bedrock_client
  6. Retorna la respuesta al chat de Telegram por medio de telegram_client

