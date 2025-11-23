import asyncio
from src.orchestrator.research_manager import ResearchManager

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

async def main():
    async for chunk in run("What is 3I/Atlas?"):
        # print(chunk)
        pass

if __name__ == "__main__":
    asyncio.run(main())
