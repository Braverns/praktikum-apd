huruf_A = [
    '    /\\ ',
    '     /  \\ ',
    '     /    \\ ',
    '     /      \\ ',
    '     /--------\\ ',
    '     /          \\ ',
    '     /            \\ ',
    '     /              \\ '
]

huruf_B = [
    '|‾‾‾‾‾‾‾‾‾\\ ',
    '|          \\ ',
    '|          |',
    '|         / ',
    '|---------\\ ',
    '|          \\ ',
    '|           |',
    '|           |',
    '|__________/ '
]

huruf_C = [
    '      __________',
    '       /          \\ ',
    ' /         ',
    '|          ',
    '|          ',
    '|          ',
    ' \\         ',
    '     \\          /',
    '      ‾‾‾‾‾‾‾‾‾‾ '
]

huruf_D = [
    '|‾‾‾‾‾‾‾‾‾‾\\',
    '  |           \\ ',
    '   |            \\ ',
    '   |             |',
    '   |             |',
    '   |             |',
    '   |            / ',
    '  |           / ',
    '|__________/ '
]

huruf_dict = {
    'A': huruf_A,
    'B': huruf_B,
    'C': huruf_C,
    'D': huruf_D
}



senjata = {}
next_id_senjata = 1
next_id_senjata_m = 1

data_murid = {}

panjang = f'|{' '*105}|'
tengah =  f'|{'_'*105}|'
atas = f'{'_'*107}'

RESET = "\033[0m"
BOLD = "\033[1m"
GOLD = "\033[93m"
CYAN = "\033[96m"
PURPLE = '\033[95m'
RED = '\033[91m'
BLUE = '\033[34m'
GREEN = '\033[32m'
GRAY = '\033[90m'
BLACK = '\033[30m'
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
WHITE = '\033[97m'
BORDER_COLOR = "\033[94m"