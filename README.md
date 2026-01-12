# mcp-client

Cliente MCP (Model Context Protocol) que conecta un LLM con el servidor BDNS para buscar ayudas y subvenciones españolas mediante conversación natural.

## ¿Qué hace?

Este proyecto permite chatear con un asistente AI que puede buscar y consultar convocatorias de ayudas del BDNS (Base de Datos Nacional de Subvenciones). El asistente usa herramientas MCP para obtener información actualizada y responder a tus preguntas.

## Requisitos

- Python 3.8+
- Cuenta en [OpenRouter](https://openrouter.ai/) con API key
- Servidor MCP BDNS instalado (`bdns_mcp`)

## Instalación

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` o exporta la variable de entorno:

```bash
export OPENROUTER_API_KEY="tu-api-key-aqui"
```

## Uso

```bash
python main.py
```

El asistente se iniciará y mostrará las herramientas disponibles. Escribe tus preguntas y el asistente usará las herramientas MCP para buscar información.

Ejemplo:
```
Tú: Busca ayudas para pymes en Aragón
[MCP] Ejecutando buscar_ayudas {...}
Asistente: He encontrado 5 convocatorias abiertas para pymes en Aragón...
```

Escribe `exit` para salir.

## Estructura del proyecto

```
mcp-client/
├── main.py           # Punto de entrada y bucle principal
├── config.py         # Configuración del servidor MCP y LLM
├── llm_client.py     # Cliente para OpenRouter
└── mcp_handler.py    # Gestión de herramientas MCP
```

## Tecnologías

- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) - Protocolo para conectar LLMs con herramientas
- [OpenRouter](https://openrouter.ai/) - API para acceder a múltiples LLMs
- [BDNS MCP Server](https://github.com/AmOrFeU86/bdns-mcp) - Servidor MCP para consultar ayudas españolas
