KEYS = (
    '#',
    'B-', 'P-', 'M-', 'F-', 'X-', 'I-', 'W-', 'A-', 'E-', 'N-', 'G-', 'Z-',
    '-B', '-P', '-M', '-F', '-X', '-I', '-W', '-A', '-E', '-N', '-G', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'N-': '5-',
    'A-': '4-',
    'I-': '3-',
    'M-': '2-',
    'B-': '1-',
    'P-': '6-',
    'F-': '7-',
    'W-': '8-',
    'E-': '9-',
    'G-': '0-',
    '-B': '1-',
    '-M': '2-',
    '-I': '3-',
    '-A': '4-',
    '-N': '5-',
    '-P': '6-',
    '-F': '7-',
    '-W': '8-',
    '-E': '9-',
    '-G': '0-',
}

UNDO_STROKE_STENO = "X-X"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'N-': 'q',
        'G-': 'a',
        'A-': 'w',
        'E-': 's',
        'I-': 'e',
        'W-': 'd',
        'M-': 'r',
        'F-': 'f',
        'B-': 't',
        'P-': 'g',
        'Z-': 'c',
        'X-': 'v',

        '-X': 'n',
        '-Z': 'm',
        '-B': 'y',
        '-P': 'h',
        '-M': 'u',
        '-F': 'j',
        '-I': 'i',
        '-W': 'k',
        '-A': 'o',
        '-E': 'l',
        '-N': 'p',
        '-G': ';',

        'arpeggiate': 'space',
        'no-op': ('B'),
    },
    'Gemini PR': {
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

        'no-op': ('-D','-Z','res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = './dictionaries/'
DEFAULT_DICTIONARIES = (
	'Combined_index.json'
	'Combined_conflict.json'
	'Combined_main.json'

)
