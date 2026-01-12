import json


class MCPHandler:
    def __init__(self, session):
        self.session = session

    def format_tools_for_llm(self, tools):
        """Convierte herramientas MCP al formato OpenAI"""
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema
                }
            }
            for tool in tools
        ]

    async def process_tool_calls(self, tool_calls, conversation):
        """Ejecuta las herramientas y añade los resultados a la conversación"""
        for call in tool_calls:
            tool_name = call["function"]["name"]
            tool_args = json.loads(call["function"]["arguments"])

            print(f"[MCP] Ejecutando {tool_name} {tool_args}")

            # Ejecutar herramienta
            result = await self.session.call_tool(tool_name, tool_args)
            text_result = "\n".join([c.text for c in result.content if hasattr(c, 'text')])

            # Añadir resultado a la conversación
            conversation.append({
                "role": "tool",
                "tool_call_id": call["id"],
                "content": text_result
            })
