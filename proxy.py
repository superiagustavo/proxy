from fastapi import FastAPI, Request
import httpx

app = FastAPI()
RENDER_API_URL = "https://shayajean-backend.onrender.com"

@app.post("/generate-pdf")
async def proxy_generate_pdf(request: Request):
    try:
        payload = await request.json()
        print("🔁 REQUISIÇÃO DO GPT:", payload)

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{RENDER_API_URL}/generate-pdf",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

        print("✅ RESPOSTA DO BACKEND:", response.text)
        return response.json()

    except Exception as e:
        print("❌ ERRO AO ENVIAR PARA O BACKEND:", str(e))
        return {"erro": str(e)}

