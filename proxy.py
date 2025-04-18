from fastapi import FastAPI, Request
import httpx

app = FastAPI()
RENDER_API_URL = "https://shayajean-backend.onrender.com"  # seu backend real

@app.post("/generate-pdf")
async def proxy_generate_pdf(request: Request):
    try:
        payload = await request.json()

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{RENDER_API_URL}/generate-pdf",
                json=payload,
                timeout=30
            )

        return response.json()
    except Exception as e:
        return {"erro": str(e)}
