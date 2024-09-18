from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Fonction de gestion du message /start
async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bienvenue LUCKYJETPROGRAMMA!")
    await update.message.reply_text("Pour afficher la table de multiplication d'un nombre, envoyer-moi un message avec la commande /table suivi du nombre.")

# Fonction de gestion du message /table
async def multiplication_table(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        number = int(context.args[0])
        table = f"Voici la table de multiplication de {number} :\n"
        for i in range(1, 11):
            table += f"{number} x {i} = {number * i}\n"
        await update.message.reply_text(table)
    except (IndexError, ValueError):
        await update.message.reply_text("Veuillez fournir un nombre valide après la commande /table.")

# Lancement du bot
if name == 'main':
    app = ApplicationBuilder().token('7024310086:AAEgzBbJfcmEuM8GftOwjy6VCUmHOs6UTTI').build()
    app.add_handler(CommandHandler("start", welcome_message))
    app.add_handler(CommandHandler("table", multiplication_table))
    app.run_polling()
