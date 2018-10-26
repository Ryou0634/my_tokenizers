import os
import logging
logger = logging.getLogger()

def _call_perl_script(script, filename):
    logger.info('Call '+script+'.perl')
    logger.info('Processing ' + filename+' ...')
    path = os.path.dirname(os.path.abspath(__file__))
    os.system('perl '+path+'/../mosesdecoder/scripts/tokenizer/'+script+'.perl < '+filename+' > '+filename+'.tmp')
    os.system('mv '+filename+'.tmp '+filename)

def deescape_special_chars(filename):
    _call_perl_script('deescape-special-chars', filename)

def normalize_punctuation(filename):
    _call_perl_script('normalize-punctuation', filename)

def replace_unicode_punctuation(filename):
    _call_perl_script('replace-unicode-punctuation', filename)

def remove_non_printing_char(filename):
    _call_perl_script('remove-non-printing-char', filename)

