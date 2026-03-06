from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.graph.healthbot_graph import HealthBotGraph

router = APIRouter()


@router.post("/chat")
async def chat(topic: str):

    graph = HealthBotGraph()

    async def event_stream():

        state = {"topic": topic}

        for event in graph.graph.stream(state):

            yield f"data: {event}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
    )