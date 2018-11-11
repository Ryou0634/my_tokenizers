from mosestokenizer import MosesTokenizer

class TokenizerBase():
    def __init__(self, language, lower=True):
        self.tokenizer = MosesTokenizer(lang=language)
        self.lower = lower

    def __call__(self, text):
        '''
        Prameters
        ---------
        text : str

        Return
        ------
        tokenized : List[str]
        '''
        # lower
        if self.lower:
            text = text.lower()
        # moses tokenizer
        tokenized = self.tokenizer(text)
        return tokenized


class EnglishTokenizer(TokenizerBase):
    def __init__(self, lower=True):
        super().__init__(language='en')

class FrenchTokenizer(TokenizerBase):
    def __init__(self, lower=True):
        super().__init__(language='fr')

class GermanTokenizer(TokenizerBase):
    def __init__(self, lower=True):
        super().__init__(language='de')

if __name__ == '__main__':
    tokenizer = EnglishTokenizer()
    text = "It was A Big H's ProbLem."
    print(tokenizer(text))

    tokenizer = FrenchTokenizer()
    text = "J'ai appris l'essentiel de la grammaire française en six mois."
    print(tokenizer(text))
