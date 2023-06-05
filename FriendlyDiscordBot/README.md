# FriendlyDiscordBot

A Discord bot that gets triggered with the command `-gpt` and sends a message using the OpenAI API.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/FriendlyDiscordBot.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your Discord bot token and OpenAI API key:

```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Run the bot:

```
python main.py
```

2. Invite the bot to your Discord server.

3. Use the `-gpt` command followed by your message to trigger the bot:

```
-gpt Your message here
```

The bot will send a message using the OpenAI API with the system prompt "A Friendly bot" and the user prompt as the message sent by the user.