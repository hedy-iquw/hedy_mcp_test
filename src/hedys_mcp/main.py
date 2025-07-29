from .server import server
from mcp.server.stdio import stdio_server

import asyncio

app = server.app  # Expose the ASGI app for uvicorn

# Optionally, provide a main for running as a script
if __name__ == "__main__":
    async def run():
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream)
    asyncio.run(run())
