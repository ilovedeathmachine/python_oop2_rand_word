import random

class WordFinder:

    def __init_(self, path):

        dict_file = open(path)

        self.words = self.parse(words.txt)

        print(f"{len(self.words)} words read")

    def parse(self, words.txt):

        return [w.strip() for w in words.txt]
    
    def random(self):

        return random.choice(self.word)
    

class SpecialWordFinder(WordFinder):

    def parse(self, words.txt):
        """Parse dict_file -> list of words, skipping blanks & cmnts"""

        return [w.strip() for w in words.txt
                if w.strip() and not w.startswith("#")]