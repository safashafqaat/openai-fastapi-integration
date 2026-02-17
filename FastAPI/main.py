from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import httpx
import asyncio

app = FastAPI(title="OpenAI Integration API")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment variables.")

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    prompt: str
    ai_response: str


@app.post("/chat", response_model=PromptResponse)
async def chat_with_openai(request: PromptRequest):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": request.prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()
            resp_json = response.json()

        ai_text = resp_json["choices"][0]["message"]["content"].strip()

        return PromptResponse(
            prompt=request.prompt,
            ai_response=ai_text
        )

    except httpx.HTTPStatusError as exc:
 
        raise HTTPException(status_code=exc.response.status_code, detail=f"OpenAI API error: {exc.response.text}")
    except httpx.RequestError as exc:

        raise HTTPException(status_code=500, detail=f"Request failed: {exc}")
    except Exception as exc:

        raise HTTPException(status_code=500, detail=f"Unexpected error: {exc}")
