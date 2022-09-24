'''from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

CHANNELS = ["-1001541827460"]'''

import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot toekn
ADMINS= [5214383653,737003043]  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili

CHANNELS = ["-1001541827460"]
