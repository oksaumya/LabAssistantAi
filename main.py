import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sse_starlette.sse import EventSourceResponse

from rag import initialize_rag


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.rag_chain = initialize_rag()
    yield


app = FastAPI(title="Lab Assistant AI", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.get("/chat")
async def chat(query: str = Query(..., min_length=1)):
    chain = app.state.rag_chain

    async def event_generator():
        try:
            async for token in chain.astream(query):
                yield {"data": token}
                await asyncio.sleep(0)
            yield {"data": "[DONE]"}
        except Exception as e:
            yield {"data": f"Error: {str(e)}"}
            yield {"data": "[DONE]"}

    return EventSourceResponse(event_generator())
