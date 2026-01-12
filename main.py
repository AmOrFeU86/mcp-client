import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client

from config import BDNS_CONFIG
from llm_client import LLMClient
from mcp_handler import MCPHandler


async def process_user_message(
    user_input: str,
    conversation: list,
    llm: LLMClient,
    mcp: MCPHandler,
    tools: list
):
    """Procesa un mensaje del usuario y genera una respuesta"""
    conversation.append({"role": "user", "content": user_input})

    llm_tools = mcp.format_tools_for_llm(tools)

    response = llm.call(conversation, llm_tools)
    message = response["choices"][0]["message"]

    if "tool_calls" in message:
        conversation.append(message)
        await mcp.process_tool_calls(message["tool_calls"], conversation)

        print("[LLM] Procesando resultados...")
        final_response = llm.call(conversation)
        final_text = llm.get_message_content(final_response)

        if final_text:
            conversation.append({"role": "assistant", "content": final_text})
            print(f"\nAsistente: {final_text}\n")
        else:
            print("Asistente: No he podido procesar la respuesta final.\n")
    else:
        assistant_text = message["content"]
        conversation.append({"role": "assistant", "content": assistant_text})
        print(f"Asistente: {assistant_text}\n")


async def main():
    """Función principal del agente"""
    conversation = []

    async with stdio_client(BDNS_CONFIG) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            llm = LLMClient()
            mcp = MCPHandler(session)

            tools = (await session.list_tools()).tools
            print("[MCP] Tools disponibles:")
            for tool in tools:
                print(f" - {tool.name}")

            print("\nAgente MCP iniciado (bdns)")
            print("Escribe 'exit' para salir\n")

            while True:
                user_input = await asyncio.to_thread(input, "Tú: ")
                user_input = user_input.strip()

                if user_input.lower() in ("exit", "quit"):
                    break

                await process_user_message(user_input, conversation, llm, mcp, tools)


if __name__ == "__main__":
    asyncio.run(main())
