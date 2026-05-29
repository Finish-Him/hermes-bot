# Deploy Hermes Bot to VPS via GitHub Actions

## Setup SSH Key for Deploy

1. **Generate deploy key on local machine:**
```bash
ssh-keygen -t ed25519 -f deploy_key -N "" -C "hermes-bot-deploy"
```

2. **Add public key to VPS:**
```bash
cat deploy_key.pub | ssh root@187.77.37.158 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

3. **Add private key to GitHub Secrets:**
   - Go to: https://github.com/Finish-Him/hermes-bot/settings/secrets
   - Add `VPS_DEPLOY_KEY` with the content of `deploy_key`

## Testing

Push to main branch or run workflow manually:
https://github.com/Finish-Him/hermes-bot/actions

## Manual Deploy on VPS

```bash
cd /opt/hermes-bot
./deploy.sh
```

## Bot Commands

- `/start` - Iniciar conversa
- `/help` - Ajuda
- `/ping` - Status
- `/echo <texto>` - Repetir
