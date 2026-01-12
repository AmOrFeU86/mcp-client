import os
from mcp import StdioServerParameters

# Configuración del servidor MCP (BDNS)
BDNS_CONFIG = StdioServerParameters(
    command="python",
    args=["-m", "bdns_mcp.server"],
    env=os.environ.copy()
)

# Configuración del LLM (OpenRouter)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "x-ai/grok-4.1-fast"

# Headers para las peticiones HTTP
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "bdns-mcp-agent"
}
