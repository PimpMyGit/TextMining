import re
import string
import html

import nltk
from nltk.corpus import stopwords; nltk.download('stopwords');

from comodo.comodo.comodo import *

# --------------------------------------------------------------------------- #

comodo_config = {

    'PATHS' : {
        '_CSV_DIR' :    PATHS._BASE_DIR + '\\csv\\'
    },

    'MODULES' : {},

    'OBJECTS': {

        '_PREPROCESS_STEPS' : {
            'LOWER':            lambda s:   s.lower(),                                                                                                      # Minuscolo grazie, microfono fibra, ah
            'NO_QUOTE':         lambda s:   s[(1 if s[0]=='"' else 0) : (-1 if s[-1]=='"' else len(s))],                                                    # Rimozione apici inizio e fine
            'DECODE_HTML':      lambda s:   html.unescape(s),                                                                                               # Caratteri speciali
            'NO_URL':           lambda s:   re.sub(r'https?://\S+|www.\.\S+', '', s),                                                                       # No urls
            'NO_EMOJI':         lambda s:   UTILS.one_space(re.compile("["                                                                                  # No emoticon
                                                        u"\U0001F600-\U0001F64F" 
                                                        u"\U0001F300-\U0001F5FF" 
                                                        u"\U0001F680-\U0001F6FF" 
                                                        u"\U0001F1E0-\U0001F1FF" 
                                                        u"\U00002500-\U00002BEF" 
                                                        u"\U00002702-\U000027B0"
                                                        u"\U00002702-\U000027B0"
                                                        u"\U000024C2-\U0001F251"
                                                        u"\U0001f926-\U0001f937"
                                                        u"\U00010000-\U0010ffff"
                                                        u"\u2640-\u2642"
                                                        u"\u2600-\u2B55"
                                                        u"\u200d"
                                                        u"\u23cf"
                                                        u"\u23e9"
                                                        u"\u231a"
                                                        u"\ufe0f"
                                                        u"\u3030"
                                                        "]+", flags=re.UNICODE).sub(r' ', s)),
            'NO_ESCAPE':        lambda s:   UTILS.one_space(UTILS.str_replace(s, {'\n':' ', '\r':' ', '\t':' '})),                                          # Cursori vari
            'NO_PUNCTUATION':   lambda s:   UTILS.one_space(UTILS.str_replace(s, {                                                                          # Punteggiatura
                                                                                    '!'     :   ' ',
                                                                                    '"'     :   ' ',
                                                                                    '#'     :   ' ',
                                                                                    '$'     :   ' ',
                                                                                    '%'     :   ' ',
                                                                                    '&'     :   ' ',
                                                                                    '\''    :   '\'',
                                                                                    '('     :   ' ',
                                                                                    ')'     :   ' ',
                                                                                    '*'     :   ' ',
                                                                                    '+'     :   ' ',
                                                                                    ','     :   ' ',

                                                                                    ' - '   :   ' ',
                                                                                    '- '    :   ' ', 
                                                                                    ' -'    :   ' ',
                                                                                    '-'     :   '_',

                                                                                    '/'     :   ' ',
                                                                                    ':'     :   ' ',
                                                                                    ';'     :   ' ',
                                                                                    '<'     :   ' ',
                                                                                    '='     :   ' ',
                                                                                    '>'     :   ' ',
                                                                                    '?'     :   ' ',
                                                                                    '['     :   ' ',
                                                                                    '\''    :   ' ',
                                                                                    ']'     :   ' ',
                                                                                    '^'     :   ' ',
                                                                                    '_'     :   ' ',
                                                                                    '`'     :   ' ',
                                                                                    '{'     :   ' ',
                                                                                    '|'     :   ' ',
                                                                                    '}'     :   ' ',
                                                                                    '~'     :   ' ',
                                                                                })),
            'NO_NUMBERS':       lambda s:   UTILS.one_space(re.sub(r'(\d\d*\.?)+', ' ', s)),                                                                    # Numeri
            'NO_ELLIPSIS':      lambda s:   UTILS.one_space(re.sub(r'\.{2,}', '. ', s)),                                                                     # Puntini di sospensione
            # 'NO_STOP_WORDS':    lambda s:   UTILS.one_space(' '.join(LIST.lfilter(s.split(), lambda w: w not in stopwords))),                                 # Rimozione stopwords
        },

        '_POS_TAG': {
            'ALL': [
                'CC',       # NO    # coordinating conjunction
                'CD',       # NO    # cardinal digit
                'DT',       # NO    # determiner

                'EX',       # NO    # existential there (like: “there is” … think of it like “there exists”)
                'FW',       # NO    # foreign word
                'IN',       # NO    # preposition/subordinating conjunction

                'JJ',       # adjective ‘big’
                'JJR',      # adjective, comparative ‘bigger’
                'JJS',      # adjective, superlative ‘biggest’

                'LS',       # NO    # list marker 1)

                'MD',       # NO    # modal could, will

                'NN',       # noun, singular ‘desk’
                'NNS',      # noun plural ‘desks’

                'NNP',      # proper noun, singular ‘Harrison’
                'NNPS',     # proper noun, plural ‘Americans’

                'PDT',      # NO    # predeterminer ‘all the kids’
                'POS',      # NO    # possessive ending parent’s
                'PRP',      # NO    # personal pronoun I, he, she
                'PRP$',     # NO    # possessive pronoun my, his, hers

                'RB',       # adverb very, silently,
                'RBR',      # adverb, comparative better
                'RBS',      # adverb, superlative best
                'RP',       # particle give up

                'TO',       # NO    # to go ‘to’ the store.
                'UH',       # NO    # interjection, errrrrrrrm

                'VB',       # verb, base form take
                'VBD',      # verb, past tense took
                'VBG',      # verb, gerund/present participle taking
                'VBN',      # verb, past participle taken
                'VBP',      # verb, sing. present, non-3d take
                'VBZ',      # verb, 3rd person sing. present takes

                'WDT',      # NO    # wh-determiner which
                'WP',       # NO    # wh-pronoun who, what
                'WP$',      # NO    # possessive wh-pronoun whose
                'WRB'       # NO    # wh-abverb where, when
            ],
            'TO_KEEP': [
                'JJ',       # adjective ‘big’
                'JJR',      # adjective, comparative ‘bigger’
                'JJS',      # adjective, superlative ‘biggest’

                'NN',       # noun, singular ‘desk’
                'NNS',      # noun plural ‘desks’
                'NNP',      # proper noun, singular ‘Harrison’
                'NNPS',     # proper noun, plural ‘Americans’

                'RB',       # adverb very, silently,
                'RBR',      # adverb, comparative better
                'RBS',      # adverb, superlative best
                'RP',       # particle give up

                'VB',       # verb, base form take
                'VBD',      # verb, past tense took
                'VBG',      # verb, gerund/present participle taking
                'VBN',      # verb, past participle taken
                'VBP',      # verb, sing. present, non-3d take
                'VBZ'       # verb, 3rd person sing. present takes
            ]  
        },   

        '_STOPWORDS': list(set(stopwords.words('english'))),
        '_NEG_STOPWORDS': [
            "hasn",
            "not",
            "won",
            "mightn't",
            "is'",
            "aren",
            "wouldn",
            "wouldn't",
            "needn",
            "shouldn",
            "wasn't",
            "don't",
            "hadn't",
            "hadn",
            "weren't",
            "won't",
            "shouldn't",
            "isn't",
            "no",
            "nor",
            "ain",
            "isn",
            "doesn't",
            "mightn",
            "aren't",
            "shan't",
            "couldn't",
            "doesn",
            "hasn't",
            "haven't",
            "didn't",
            "mustn",
            "needn't",
            "mustn't",
            "couldn",
            "don"
        ], 

        '_FINAL_PREP_OP': {
            'DELETE': [
                '•full•',
                '•feeling',
                '•fatigued',
                '•extreme',
                '•effectiveness',
                '•dizziness',
                '•diffuctly',
                '•diarrhea',
                '•dehabiliting',
                '•anxiety',
                '•abdominal',
'               .a',
                '.able',
                '.about',
                '.actually',
                '.advil',
                '.afraid',
                '.after',
                '.all',
                '.also',
                '.always',
                '.and',
                '.as',
                '.at',
                '.back',
                '.bad',
                '.be',
                '.been',
                '.began',
                '.but',
                '.buy',
                '.by',
                '.chlorpheniramine',
                '.cirrossis',
                '.compared',
                '.complete',
                '.con',
                '.constella',
                '.costing',
                '.daily',
                '.day',
                '.definatly',
                '.despite',
                '.do',
                '.doctor',
                '.don',
                '.dont',
                '.dr',
                '.dry',
                '.ended',
                '.erections',
                '.even',
                '.every',
                '.everything',
                '.experienced',
                '.fast',
                '.feeling',
                '.felt',
                '.five',
                '.food',
                '.for',
                '.goal',
                '.god',
                '.good',
                '.great',
                '.hard',
                '.has',
                '.have',
                '.havent',
                '.having',
                '.havnt',
                '.he',
                '.headaches',
                '.hehe',
                '.help',
                '.helpless',
                '.honestly',
                '.hope',
                '.hours',
                '.how',
                '.hysingla',
                '.i',
                '.iam',
                '.if',
                '.im',
                '.in',
                '.indigestion',
                '.influenza',
                '.injecting',
                '.it',
                '.its',
                '.iud',
                '.joy',
                '.just',
                '.knowing',
                '.l',
                '.linzess',
                '.love',
                '.lymphodema',
                '.main',
                '.missed',
                '.my',
                '.nausea',
                '.neuropathy',
                '.no',
                '.non',
                '.not',
                '.nothing',
                '.now',
                '.of',
                '.off',
                '.oh',
                '.on',
                '.only',
                '.or',
                '.pain',
                '.people',
                '.please',
                '.plus',
                '.probably',
                '.randomly',
                '.rapid',
                '.reglan',
                '.sadly',
                '.see',
                '.she',
                '.since',
                '.so',
                '.some',
                '.started',
                '.still',
                '.sunday',
                '.take',
                '.taking',
                '.thank',
                '.thanks',
                '.that',
                '.the',
                '.then',
                '.these',
                '.they',
                '.third',
                '.this',
                '.those',
                '.till',
                '.tiredness',
                '.to',
                '.today',
                '.toradol',
                '.tremors',
                '.tried',
                '.u',
                '.ultimate',
                '.up',
                '.uti',
                '.very',
                '.was',
                '.we',
                '.weight',
                '.well',
                '.went',
                '.when',
                '.which',
                '.while',
                '.white',
                '.will',
                '.wish',
                '.with',
                '.within',
                '.works',
                '.worst',
                '.wow',
                '.yea',
                '.yet',
                '.you',
                '\\arthritis',
                '\\bp',
                '\\cold',
                '\\robert',
                'a.',
                'a.a',
                'a.a.',
                'a.am',
                'a.d.',
                'a.d.d',
                'a.d.h.d',
                'a.few',
                'a.functioning',
                'a.g.e',
                'a.grill',
                'a.k.a',
                'a.l.s',
                'a.lot',
                'a.m',
                'a.m.',
                'a.r.d.s',
                'a.s',
                'a.s.',
                'a.s.a.p',
                'a.t.',
                'aa',
                'aaa',
                'aaaaaammazing',
                'aaaaand',
                'aaaaarg',
                'aaaahhhhh',
                'aaaand',
                'aaahh',
                'aaand',
                'aaccident',
                'aad',
                'aadd',
                'aaf',
                'aap',
                'aaps',
                'aarp',
                'aatd',
                'ab',
                'aba',
                '≥',
                '℅',
                '℃',
                '€',
                '′',
                '…i',
                '…',
                '•••but•••',
                '•very',
                '•not',
                '•no',
                '•increased',
                '•i',
                '•',
                '”',
                '“',
                '’',
                '‘',
                '—very',
                '—notable',
                '—it',
                '—',
                '–',
                '\u200b\u200bbetween',
                '،',
                'іt',
                'і',
                'ø',
                '÷',
                'ñife',
                'à',
                '×daily',
                '×',
                '¿',
                '¾',
                '½',
                '¼',
                'µg',
                '°f',
                '°',
                '¯\\',
                '¯',
                '£uk',
                '£',
                'zzzzzzzz',
                'zzzzz',
                'zzzzap',
                'zzzquill',
                'zzzquil',
                'zzz',
            ]
        }
    }
}           

#            --------------------------------------------------------------------------- #