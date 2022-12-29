import requests

def check_bot_status(bot_id):
    # Make a GET request to the Discord API to get the bot's user object
    response = requests.get(f"https://discordapp.com/api/users/{bot_id}")

    # If the request returns a status code of 200, the bot is online
    if response.status_code == 200:
        print("The bot is online.")
    else:
        print("The bot is offline.")

# Replace BOT_ID with the ID of your Discord bot
check_bot_status(658732840783052823)
