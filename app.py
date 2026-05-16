import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Note duas mudanças principais na criação do cliente:
client = OpenAI(
  base_url="https://openrouter.ai/api/v1", # <- 1. Endereço do OpenRouter
  api_key=os.getenv("OPENROUTER_API_KEY"),  # <- 2. Sua nova chave do OpenRouter
)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    pergunta = ""

    if request.method == "POST":
        pergunta = request.form["pergunta"]
        try:
            response = client.chat.completions.create(
                # Aqui você pode trocar de modelo com facilidade:
                model="google/gemini-2.5-flash", # Exemplo: modelo do Google
                messages=[
                    {"role": "system", "content": "Você é um assistente prestativo."},
                    {"role": "user", "content": pergunta}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            resposta = response.choices[0].message.content
        except Exception as e:
            resposta = f"Erro ao chamar a API: {e}"

    return render_template("index.html", pergunta=pergunta, resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)