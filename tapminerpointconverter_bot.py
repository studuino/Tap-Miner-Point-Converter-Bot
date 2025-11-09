from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ðŸ‘‹ *Blockdag Tap Miner Point Converter!*\n\n"
        "Follow me @bdagx1mining\n\n"
        "Buy from here : https://purchase3.blockdag.network/?ref=of3vumaf\n\n"
        "X1 Referral Code : **i4NdChP5**\n\n"
        "Tell me your Tap Points in Million (no decimals), and I'll calculate using these conversion ratios:\n"
        "â€¢ 0â€“10 Millions(M) â†’ `1:200`\n"
        "â€¢ 11â€“100 M â†’ `1:500`\n"
        "â€¢ 101â€“1,000 M(1B) â†’ `1:2000`\n"
        "â€¢ 1,001â€“10,000 M(10B) â†’ `1:5000`\n"
        "â€¢ 10,001â€“50,000 M(50B) â†’ `1:15000`\n"
        "â€¢ 50,001â€“200,000 M(200B) â†’ `1:30000`\n\n"
        "âš ï¸ Only numbers between *0 and 200,000* are valid.\n\n"
        "Example: Try input your tap points in millions like *250* ðŸ‘‡",
        parse_mode="Markdown"
    )

# Handle user input
async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Validate integer input
    if not text.isdigit():
        await update.message.reply_text(
            "ðŸš« *Invalid input!*\nPlease send a *whole number* (no negative or decimals or letters).",
            parse_mode="Markdown"
        )
        return

    x = int(text)

    # Check overall valid range
    if x < 0 or x > 200000:
        await update.message.reply_text(
            "ðŸš« *Out of range!*\nPlease enter a number between *0 and 200,000.*",
            parse_mode="Markdown"
        )
        return

    # Apply formulas based on range
    if 0 < x <= 10:
        result = x * 1000000 / 200
        formula = "1:200"
    elif 11 <= x <= 100:
        result = ((x - 10) * 1000000 / 500) + 50000
        formula = "1:500"
    elif 101 <= x <= 1000:
        result = ((x - 100) * 1000000 / 2000) + 230000
        formula = "1:2000"
    elif 1001 <= x <= 10000:
        result = ((x - 1000) * 1000000 / 5000) + 680000
        formula = "1:5000"
    elif 10001 <= x <= 50000:
        result = ((x - 10000) * 1000000 / 15000) + 6980000
        formula = "1:15000"
    elif 50001 <= x <= 200000:
        result = ((x - 50000) * 1000000 / 30000) + 37646667
        formula = "1:30000"
    else:
        await update.message.reply_text(
            "âš ï¸ *Unexpected range.* Please check your number.",
            parse_mode="Markdown"
        )
        return

    # Format result (rounded to 6 decimals for neatness)
    message = (
        f"ðŸ§® *Calculation Complete!*\n\n"
        f"â€¢ *Total Tap Points in Millions:* `{x}`\n"
        #f"â€¢ *Formula Used:* `{formula}`\n"
        f"â€¢ *Converted BDAG Coins:* `{round(result):,}`"
    )

    await update.message.reply_text(message, parse_mode="Markdown")

# Main function
def main():
    
    #import os
    #TOKEN = os.getenv("BOT_TOKEN")

    from dotenv import load_dotenv
    import os

    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    
    #TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace this with your BotFather token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("Start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

    print("ðŸ¤– Blockdag Tap Point Converter Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
