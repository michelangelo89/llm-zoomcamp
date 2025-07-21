from fastmcp import Client
from fastmcp.client.transports import StdioTransport
import asyncio

async def main():
    # ✅ Pass command as a string, not a list
    transport = StdioTransport(command="python", args=["weather_server.py"])
    
    async with Client(transport=transport) as mcp_client:
        print("✅ Connected to MCP server!")

        # Step 1: Get list of tools
        tools = await mcp_client.list_tools()
        print("🛠️ Available tools:")
        print(tools)

        # Step 2: Call the 'get_weather' tool with city = 'Berlin'
        result = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print("\n🌤️ Weather in Berlin:")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())