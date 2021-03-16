"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:

    def __init__(self, pathfile):
        self.words = []
        with open(pathfile, 'r') as file:
            for line in file:
                self.words.append(line.strip())

        print(f'{self.word_count()} words read')

    def random(self):
        return choice(self.words)

    def word_count(self):
        return len(self.words)


class SpecialWordFinder(WordFinder):

    def __init__(self, pathfile):
        self.words = []
        with open(pathfile, 'r') as file:
            for line in file:
                if line[0] is not ("#" or "\n"):
                    self.words.append(line.strip())

        print(f'{self.word_count()} words read')
    
    def random(self):
        super(SpecialWordFinder, self).random()

    def word_count(self):
        super(SpecialWordFinder, self).word_count()