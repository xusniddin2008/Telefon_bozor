from aiogram import Dispatcher

from loader import dp
# from .throttling import ThrottlingMiddleware


# if __name__ == "middlewares":
#     dp.middleware.setup(ThrottlingMiddleware())


from aiogram import Dispatcher

from loader import dp
from .checksub import BigBrother


if __name__ == "middlewares":
    dp.middleware.setup(BigBrother())

