"""Remove messages with mention from chat

This app implements logic of removing messages with mention
For now it removes messages after 10 sec
Also it removes messages elder 24 hours
To remove old messages send "$delete_old_mes" to discord chat
"""

import apps.remove_bot.app
