#!/usr/bin/env python3
import os, logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8776559084:AAE_oE-mtXdPxx00mIpcUPqDACxJ1mGsNSg"
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update, ctx):
    u = update.effective_user
    await update.message.reply_text("Olá " + u.full_name + "! Sou Hermes 🪐", parse_mode="Markdown")

async def help_cmd(update, ctx):
    await update.message.reply_text("📚 /start /help /ping /echo <texto>", parse_mode="Markdown")

async def ping(update, ctx):
    import time
    start = time.time()
    msg = await update.message.reply_text("🏃...")
    await msg.edit_text("✅ Online! " + str(round((time.time()-start)*1000, 2)) + "ms", parse_mode="Markdown")

async def echo(update, ctx):
    text = " ".join(ctx.args) if ctx.args else "Use /echo <texto>"
    await update.message.reply_text("🔄 " + text)

async def msg_handler(update, ctx):
    t = update.message.text.lower()
    u = update.effective_user
    if any(g in t for g in ["oi", "olá", "hello", "hi"]): r = "Olá, " + u.first_name + "! 😊"
    elif "obrigado" in t: r = "De nada! 🙏"
    elif "quem é você" in t: r = "Sou o Hermes, mensageiro! 🪐"
    else: r = "📨 Recebi: '" + update.message.text + "'\nComo posso ajudar?"
    await update.message.reply_text(r, parse_mode="Markdown")

def main():
    print("🚀 Hermes Bot iniciando...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg_handler))
    print("✅ Hermes online!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__": main()
