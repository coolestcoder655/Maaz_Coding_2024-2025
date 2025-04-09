from colorama import Style, Fore
from selenium.webdriver.support.color import Color

all_fore_colors = [attr for attr in dir(Fore) if not attr.startswith("_")]
Fores = [Fore.BLACK, Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA, Color.CYAN, Color.WHITE]


all_styles = [attr for attr in dir(Style) if not attr.startswith("_")]

print(all_fore_colors)
print(all_styles)