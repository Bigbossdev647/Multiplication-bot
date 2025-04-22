import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from fpdf import FPDF

# Configurez le journal des activités
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Fonction pour générer un PDF de la table de multiplication
def generate_multiplication_table_pdf(number):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Table de multiplication de {number}", ln=True, align='C')

    for i in range(1, 11):
        result = number * i
        pdf.cell(0, 10, txt=f"{number} x {i} = {result}", ln=True)

    pdf_file_name = f"multiplication_table_{number}.pdf"
    pdf.output(pdf_file_name)
    return pdf_file_name

# Fonction de démarrage
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bienvenue ! Envoyez-moi un nombre pour obtenir sa table de multiplication au format PDF.")

# Fonction pour gérer les messages texte
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        number = int(update.message.text)
        pdf_file = generate_multiplication_table_pdf(number)
        with open(pdf_file, 'rb') as file:
            await update.message.reply_document(document=file)
    except ValueError:
        await update.message.reply_text("Veuillez entrer un nombre valide.")

# Fonction principale pour exécuter le bot
def main() -> None:
    # Remplacez 'YOUR_TOKEN' par le token de votre bot
    application = ApplicationBuilder().token("7024310086:AAEgzBbJfcmEuM8GftOwjy6VCUmHOs6UTTI").build()

    # Commande /start
    application.add_handler(CommandHandler("start", start))

    # Gestionnaire de messages texte
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Démarrez le bot
    application.run_polling()

if __name__ == '__main__':
    main()
