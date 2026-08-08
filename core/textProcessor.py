import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class TextProcessor:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))


    def clean_text(self, text):
        text = text.lower()
        text = text.translate(
        str.maketrans("", "", string.punctuation))
        return text


    def tokenize_text(self, text):
        tokens = word_tokenize(text)
        return tokens


    def remove_stopwords(self, tokens):
       filtered_tokens = []
       for token in tokens:
          if token not in self.stop_words:
            filtered_tokens.append(token)

       return filtered_tokens


    def process_text(self, text):
        text = self.clean_text(text)
        tokens = self.tokenize_text(text)
        tokens = self.remove_stopwords(tokens)
        return tokens

