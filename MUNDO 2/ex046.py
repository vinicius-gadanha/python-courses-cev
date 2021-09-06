from time import sleep
import emoji
from datetime import date
for contagem in range(10, -1, -1):
    print('\033[1;30m', contagem)
    sleep(1)
print(emoji.emojize(':tada::tada:' * 5, use_aliases=True))
print('\033[1;33m  FELIZ {}!!!\033[1;30m'.format(date.today().year + 1))
print(emoji.emojize(':tada::tada:' * 5, use_aliases=True))
