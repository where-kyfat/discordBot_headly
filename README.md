# Discord bot

---

**_Discord bot which responds: "hello, @some_user", to the user who calls it_**

**_Also implements logic of remove summoning messages_**

## Local install 

- Need to install before:
  * Python 3.9 
  * [Docker Desktop](https://docs.docker.com/desktop/#download-and-install)
- Also need to create bot on https://discord.com/developers/applications and [add](https://vc.ru/services/288966-bot-discord-kak-sozdat-i-dobavit-na-server) it to some discord server
- [Create virtual environments, activate it](https://docs.python.org/3/library/venv.html#creating-virtual-environments) and install libs from requirements:
```commandline
pip install -r requirements.txt
```
- Open `configs/bot_token.json` and write down [bot token information](https://discord.com/developers/applications):
  * token
  * bot name
  * application id
  * prefix for bot commands

P.S. if you want to ignore changes in `configs/bot_token.json` by git, run following command:
```commandline
git update-index --assume-unchanged configs/bot_token.json
```
- Build docker images:
```commandline 
docker-compose build
```

## Local start

### Only local logic (without docker)

- Activate venv by following command (replace ```venv``` with venv directory):
```commandline
venv\bin\Scripts\activate
```

- Start app:
```commandline
 python main.py
 ```

### Docker

- Deploy:
```commandline
docker-compose up -d
```
- Stop application:
```commandline
docker-compose down
```
