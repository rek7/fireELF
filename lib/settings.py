import colorama



colorama.init(autoreset=True)


VERSION = 1.0
PAYLOAD_DIR = "payloads/"

RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
WHITE = colorama.Fore.WHITE

def banner():
    # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=fireELF
    print("""{}  _____.__               ___________.____   ___________ {}{{ {}V{} {}}}{}
_/ ____\__|______   ____ \_   _____/|    |  \_   _____/
\   __\|  \_  __ \_/ __ \ |    __)_ |    |   |    __)  
 |  |  |  ||  | \/\  ___/ |        \|    |___|     \   
 |__|  |__||__|    \___  >_______  /|_______ \___  /   
                       \/        \/         \/   \/{}\thttps://github.com/rek7/fireELF""".format(RED, YELLOW, BLUE, VERSION, YELLOW, RED, WHITE))