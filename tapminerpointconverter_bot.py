from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Blockdag Tap Miner Point Converter!*\n\n"
        "Tell me your Tap Points in Million (no decimals), and I'll calculate using these conversion ratios:\n"
        "• 0–10 Millions → `1 : 200`\n"
        "• 11–100 Millions → `1 : 500`\n"
        "• 101–1000 Millions → `1 : 2000`\n"
        "• 1001–10000 Millions → `1 : 5000`\n"
        "• 10001–50000 Millions → `1 : 15000`\n"
        "• 50001–200000 Millions → `1 : 30000`\n\n"
        "⚠️ Only numbers between *0 and 200,000* are valid.\n\n"
        "Example: try sending *310* 👇",
        parse_mode="Markdown"
    )

# Handle user input
async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Validate integer input
    if not text.isdigit():
        await update.message.reply_text(
            "🚫 *Invalid input!*\nPlease send a *whole number* (no decimals or letters).",
            parse_mode="Markdown"
        )
        return

    x = int(text)

    # Check overall valid range
    if x < 0 or x > 200000:
        await update.message.reply_text(
            "🚫 *Out of range!*\nPlease enter a number between *0 and 200,000.*",
            parse_mode="Markdown"
        )
        return

    # Apply formulas based on range
    if 0 <= x <= 10:
        result = x / 200
        formula = "x / 200"
    elif 11 <= x <= 100:
        result = x / 500
        formula = "x / 500"
    elif 101 <= x <= 1000:
        result = x / 2000
        formula = "x / 2000"
    elif 1001 <= x <= 10000:
        result = x / 5000
        formula = "x / 5000"
    elif 10001 <= x <= 50000:
        result = x / 15000
        formula = "x / 15000"
    elif 50001 <= x <= 200000:
        result = x / 30000
        formula = "x / 30000"
    else:
        await update.message.reply_text(
            "⚠️ *Unexpected range.* Please check your number.",
            parse_mode="Markdown"
        )
        return

    # Format result (rounded to 6 decimals for neatness)
    message = (
        f"🧮 *Calculation Complete!*\n\n"
        f"• *Input:* `{x}`\n"
        f"• *Formula Used:* `{formula}`\n"
        f"• *Result:* `{round(result, 6)}`"
    )

    await update.message.reply_text(message, parse_mode="Markdown")

# Main function
def main():
    
    import os
    TOKEN = os.getenv("BOT_TOKEN")
    
    #TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace this with your BotFather token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

    print("🤖 Smart Integer Calculator Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
