# Screen-Spy
App that helps you to get some screens from distant PC.
Contains websocket server script and telegram bot that uses client websocket script.
# Start
To start the app you should start the distant server by running server.py.
If you want to start the server automaticly you can use system deamon.

To run client create Telegram bot then create .env file in root directory. 
Fill .env with string BOT_TOKEN=<TOKEN_FROM_BOTFATHER> where <TOKEN_FROM_BOTFATHER>
is your personal API token. 
Then run bot.py: it uses /p to send you screens.

If bot have no connection to server it will send supporting log.
You can see your screens in /bot/screens

It's important to have static ip on your server.