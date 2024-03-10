from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_index.core.agent import AgentRunner
from typing import AsyncGenerator
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io

app = FastAPI()


@app.get("/stream")
async def stream_data():
    llm = Ollama(model="codellama:7b")
    agent = AgentRunner.from_llm(
        llm=llm,
        verbose=True,
    )

    messages = [
        ChatMessage(
            role="system", content="You are a pirate with a colorful personality"
        ),
    ]
    lastMessage = {"role": "user", "content": "What is your name?"}
    response = await agent.astream_chat(lastMessage["content"], messages)
    res_gen: AsyncGenerator = response.async_response_gen()

    async def event_generator():
        async for token in response.async_response_gen():
            yield token

    return StreamingResponse(event_generator(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
