KEYS = (
    '#',
    'b-', 'p-', 'm-', 'f-', 'C-', 'i-', 'w-', 'a-', 'e-', 'n-', 'g-', 'X-',
    '-b', '-p', '-m', '-f', '-C', '-i', '-w', '-a', '-e', '-n', '-g', '-X',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'n-': '1-',
    'a-': '2-',
    'i-': '3-',
    'p-': '4-',
    'b-': '5-',
    '-b': '-6',
    '-p': '-7',
    '-i': '-8',
    '-a': '-9',
    '-n': '-0',
}

UNDO_STROKE_STENO = None

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'A-': 'q',
        'O-': 'a',
        'N-': 'w',
        'E-': 's',
        'I-': 'e',
        'U-': 'd',
        'G-': 'r',
        'W-': 'f',
        'D-': 't',
        'Z-': 'g',
        'B-': 'c',
        'X-': 'v',

        '-X': 'n',
        '-B': 'm',
        '-D': 'y',
        '-Z': 'h',
        '-G': 'u',
        '-W': 'j',
        '-I': 'i',
        '-U': 'k',
        '-N': 'o',
        '-E': 'l',
        '-A': 'p',
        '-O': ';',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),

        'n-': 'S1-',
        'g-': 'S2-',
        'a-': 'T-',
        'e-': 'K-',
        'i-': 'P-',
        'w-': 'W-',
        'p-': 'H-',
        'f-': 'R-',
        'b-': '*1',
        'm-': '*2',
        'X-': 'A-',
        'C-': 'O-',

        '-C': '-E',
        '-X': '-U',
        '-b': '*3',
        '-m': '*4',
        '-p': '-F',
        '-f': '-R',
        '-i': '-P',
        '-w': '-B',
        '-a': '-L',
        '-e': '-G',
        '-n': '-T',
        '-g': '-S',

        'no-op': ('-D','Z','res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = "./"
DEFAULT_DICTIONARIES = (
    "briefs.json",
    "fingerspelling.json",
    "numbers.json",
    "punctuation.json",
    "symbols.json",
)
