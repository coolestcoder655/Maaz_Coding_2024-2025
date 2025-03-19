from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Back.RESET)
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)

print('back to normal now')

print(Style.BRIGHT + 'bold text')