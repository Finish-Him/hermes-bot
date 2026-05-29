# Hermes Bot 🤖

Telegram bot pessoal integrado com Hermes Agent.

## Setup

```bash
pip install -r requirements.txt
python hermes.py
```

## GitHub Actions

O bot pode rodar via GitHub Actions. Configure o token:
- Settings → Secrets → `TELEGRAM_BOT_TOKEN`

## Comandos

- `/start` - Iniciar
- `/help` - Ajuda
- `/ping` - Status

## Arquitetura

```
hermes-bot/
├── hermes.py        # Bot principal
├── requirements.txt # Dependências
└── .github/
    └── workflows/    # CI/CD
```
