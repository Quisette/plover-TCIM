KEYS = (
    '#',
    'B-', 'P-', 'M-', 'F-', 'X-', 'I-', 'W-', 'A-', 'E-', 'N-', 'G-', 'Z-',
    '-B', '-P', '-M', '-F', '-X', '-I', '-W', '-A', '-E', '-N', '-G', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'N-': '1',
    'A-': '2',
    'I-': '3',
    'M-': '4',
    'B-': '5',
    '-B': '6',
    '-M': '7',
    '-I': '8',
    '-A': '9',
    '-N': '0',
}

UNDO_STROKE_STENO = "X-X"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'A-': 'q',
        'O-': 'a',
        'N-': 'w',
        'E-': 's',
        'I-': 'e',
        'U-': 'd',
        'G-': 'r',
        'W-': 'F',
        'D-': 't',
        'Z-': 'G',
        'B-': 'c',
        'X-': 'v',

        '-X': 'N',
        '-B': 'M',
        '-D': 'y',
        '-Z': 'h',
        '-G': 'u',
        '-W': 'j',
        '-I': 'I',
        '-U': 'k',
        '-N': 'o',
        '-E': 'l',
        '-A': 'P',
        '-O': ';',

        'arpeggiate': 'space',
        'No-oP': ('B'),
    },
    'GEMINI PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),

        'N-': 'S1-',
        'G-': 'S2-',
        'A-': 'T-',
        'E-': 'K-',
        'I-': 'P-',
        'W-': 'W-',
        'M-': 'H-',
        'F-': 'R-',
        'B-': '*1',
        'P-': '*2',
        'Z-': 'A-',
        'X-': 'O-',

        '-X': '-E',
        '-Z': '-U',
        '-B': '*3',
        '-P': '*4',
        '-M': '-F',
        '-F': '-R',
        '-I': '-P',
        '-W': '-B',
        '-A': '-L',
        '-E': '-G',
        '-N': '-T',
        '-G': '-S',

        'no-op': ('-D','Z','res1', 'res2', 'fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = None
DEFAULT_DICTIONARIES = (

)
