import MeCab
from Mykytea import Mykytea
import unicodedata
from mojimoji import zen_to_han, han_to_zen


class JapaneseTokenizer:
    def __init__(self, tokenizer='kytea', split=True, unicode=True, half2full=True, full2half=True, lower_case=True):
        self.tokenizer = tokenizer
        if tokenizer == 'kytea':
            self.tagger = Mykytea("-deftag UNKNOWN!!")
        elif tokenizer == 'mecab':
            self.tagger = MeCab.Tagger('-Owakati')
        self.split = split
        self.unicode = unicode
        self.half2full = half2full
        self.full2half = full2half
        self.lower_case = lower_case

    def __call__(self, text):
        if self.unicode:
            text = self._normalize_unicode(text)

        if self.half2full:
            text = self._normalize_kana(text)

        if self.full2half:
            text = self._normalize_num_alphabet(text)

        if self.lower_case:
            text = self._lower_text(text)

        if self.split:
            text = self._split_words(text)

        return text

    def _normalize_unicode(self, text, form='NFKC'):
        return unicodedata.normalize(form, text)

    def _lower_text(self, text):
        return text.lower()

    def _normalize_num_alphabet(self, text):
        return zen_to_han(text, kana=False)

    def _normalize_kana(self, text):
        return han_to_zen(text, digit=False, ascii=False)

    def _split_words(self, text):
        if self.tokenizer == 'kytea':
            return list(self.tagger.getWS(text))
        elif self.tokenizer == 'mecab':
            return self.tagger.parse(text).replace('\n', '').split()


def main():
    text = '「私は９００．０円をＡＢＣﾏｰﾄから盗みました。まじですみません。」😉'
    tokenizer = JapaneseTokenizer('kytea')
    tokenized = tokenizer(text)

    print(text)
    print(tokenized)


if __name__ == '__main__':
    main()