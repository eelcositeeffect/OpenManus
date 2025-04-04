# combined.py

import asyncio
import sys
from fastapi import FastAPI
from app.agent.manus import Manus
from app.logger import logger


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OpenManus is alive!"}

async def cli_main():
    agent = Manus()
    try:
        prompt = input("Enter your prompt: ")
        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        asyncio.run(cli_main())
    else:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8055, reload=True)

