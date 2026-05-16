# 🧠 Flask + ChatGPT

Aplicação web simples desenvolvida com **Python** e **Flask** que se integra à **API do ChatGPT** (OpenAI). O projeto foi criado como parte de um desafio prático para aprender a consumir APIs de inteligência artificial generativa.

---

## 🚀 Tecnologias utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| Python | 3.8+ | Linguagem principal |
| Flask | Última estável | Framework web |
| OpenAI SDK ou OPENROUTER | Última estável | Integração com a API do ChatGPT |
| python-dotenv | Última estável | Gerenciamento de variáveis de ambiente |
| HTML5 | — | Interface web (template Jinja2) |

---

## 📁 Estrutura do projeto

```
flask-chatgpt/
├── app.py              # Código principal da aplicação Flask
├── .env                # Chave da API (não versionado — adicione ao .gitignore)
├── requirements.txt    # Dependências do projeto
├── templates/
│   └── index.html      # Interface web (formulário e resposta)
└── README.md
```

---

## ⚙️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/flask-chatgpt.git
cd flask-chatgpt
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da API

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENROUTER_API_KEY=sk-sua-chave-aqui
```

### 5. Execute a aplicação

```bash
python app.py
```

Acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador.

---

## 🧪 Como funciona

1. O usuário digita uma pergunta no campo de texto da interface web.
2. Ao enviar o formulário, o Flask captura a pergunta via `POST`.
3. A pergunta é enviada para a **API do ChatGPT** (modelo `gpt-3.5-turbo`).
4. A resposta retornada pela API é exibida na mesma página.
5. Erros comuns (cota excedida, chave inválida) são tratados e exibidos ao usuário.

---

## ❓ Resposta do desafio

**Qual é a principal necessidade para conseguir utilizar a API do ChatGPT em uma aplicação?**

> A principal necessidade é possuir uma **chave de API (API Key) válida**, gerada na plataforma da OpenAI, vinculada a uma conta com **créditos disponíveis** ou um plano de pagamento ativo.
>
> Sem essa chave autenticada e sem saldo/créditos, não é possível realizar requisições aos modelos de linguagem — todas as chamadas retornarão erro de autenticação ou cota excedida.

---

## 📝 Aprendizados

- Configurar ambiente virtual Python e gerenciar dependências com `pip`.
- Proteger credenciais sensíveis usando variáveis de ambiente com `python-dotenv`.
- Integrar uma aplicação Flask com APIs externas via HTTP.
- Tratar erros comuns: autenticação inválida, cota excedida, falhas de rede.
- Entender o fluxo de consumo de uma API de IA generativa na prática.

---