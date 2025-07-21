from fastmcp import Client
import asyncio

# This function connects to the MCP server, initializes it, and fetches the tool list
async def main():
    async with Client(["python", "weather_server.py"]) as mcp_client:
        print("✅ Connected to MCP server!")

        # Step 1: Get list of tools
        tools = await mcp_client.get_tools()
        print("🛠️ Available tools:")
        print(tools)

        # Step 2: Call the 'get_weather' tool with city = 'Berlin'
        result = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print("\n🌤️ Weather in Berlin:")
        print(result)

# Run it using asyncio
if __name__ == "__main__":
    asyncio.run(main())