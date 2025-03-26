from __future__ import annotations

import logging
from typing import Annotated
from prompts import WELCOME_MESSAGE, INSTRUCTIONS, LOOKUP_VIN_MESSAGE

import aiohttp
from api import AssistantFnc
from dotenv import load_dotenv
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    WorkerType,
    cli,
    llm,
    multimodal,
)
from livekit.plugins import google

load_dotenv('sample.env')

logger = logging.getLogger("my-worker")
logger.setLevel(logging.INFO)


async def entrypoint(ctx: JobContext):
    logger.info("starting entrypoint")

    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    participant = await ctx.wait_for_participant()
    assistant_fnc = AssistantFnc()
    chat_ctx = llm.ChatContext()
    agent = multimodal.MultimodalAgent(
        model=google.beta.realtime.RealtimeModel(
            voice="Puck",
            temperature=0.8,
            instructions=INSTRUCTIONS
        ),
        fnc_ctx=assistant_fnc,
        chat_ctx=chat_ctx,
    )
    agent.start(ctx.room, participant)
    agent.generate_reply()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, worker_type=WorkerType.ROOM))