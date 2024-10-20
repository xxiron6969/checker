from telegram import Update
from telegram.ext import Application, CommandHandler
import mysql.connector
import secrets

# MySQL Database Configuration
db_config = {
    'user': 'sql5739283',
    'password': 'LHiznJjWzE',
    'host': 'sql5.freesqldatabase.com',
    'database': 'sql5739283',
}

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(**db_config)

# Start command handler
async def start(update: Update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    
    # Generate a token
    token = secrets.token_urlsafe(16)
    
    # Store the token in the database
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, token) VALUES (%s, %s)', (username, token))
    conn.commit()
    
    # Send the login link to the user
    login_url = f"https://5280-165-154-235-209.ngrok-free.app/auth.php?token={token}"
    await update.message.reply_text(f"Hello {username}, click here to login: {login_url}")
    
    cursor.close()
    conn.close()

# Main function to start the bot
def main():
    # Your bot token from BotFather
    bot_token = "7819141961:AAFkY94jg90mfL0yGE_Qb6HxPXu77I4vaaY"

    # Create the Application instance
    application = Application.builder().token(bot_token).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Run the bot (polling mode)
    application.run_polling()

if __name__ == '__main__':
    main()
