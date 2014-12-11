import random


class Pyehuda(object):
    def __init__(self, first_list, second_list):
        if not len(first_list) and len(second_list):
            raise ValueError('Lists can not be empty')

        self.first = first_list
        self.second = second_list

    def generate(self, letter=None, matching_letters=True):
        if letter is None:
            first = random.choice(self.first)
            letter = first[0]
        else:
            first = random.choice([word for word in self.first if word[0] == letter])

        if matching_letters:
            candidates = [word for word in self.second if word[0] == letter]
        else:
            candidates = self.second

        second = random.choice(candidates)
        return first, second