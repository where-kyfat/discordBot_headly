# Discord HELLO bot

---

**_Discord bot which responds: "hello, @some_user", to the user who calls it_**

## Local install 

- Python 3.9 need to be installed before
- Also need to create bot on https://discord.com/developers/applications and [add](https://vc.ru/services/288966-bot-discord-kak-sozdat-i-dobavit-na-server) it to some discord server
- [Create virtual environments, activate it](https://docs.python.org/3/library/venv.html#creating-virtual-environments) and install libs from requirements:
```cmd
pip install -r requirements.txt
```
- Open `config.py` and write down [bot token information](https://discord.com/developers/applications):
  * token
  * bot name
  * application id
  * prefix for bot commands

## Local start

- Activate venv by following command (replace ```venv``` with venv directory):
```commandline
venv\bin\Scripts\activate
```

- Start app:
```commandline
 python main.py
 ```
