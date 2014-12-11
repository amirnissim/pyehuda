import string
import unittest

from vocabulary import adjectives, fruit
from pyehuda import Pyehuda


class PyehudaTestCase(unittest.TestCase):
    def setUp(self):
        self.alphabet = string.lowercase
        self.yehuda = Pyehuda(adjectives, fruit)

    def test_second_list_contains_all_letters_in_first_list(self):
        opening_letters_first = set(i[0] for i in self.yehuda.first)
        opening_letters_second = set(i[0] for i in self.yehuda.second)

        diff = opening_letters_first - opening_letters_second
        self.assertEqual(len(diff), 0, '{0} appear in first list but not in second'.format(diff))

    def test_matching_first_letters(self):
        codename = self.yehuda.generate(matching_letters=True)
        self.assertEqual(codename[0][0], codename[1][0], '\'{0}\' first letters are not equal')

    def test_given_letter(self):
        possible = set(f[0] for f in self.yehuda.first)
        for c in possible:
            codename = self.yehuda.generate(letter=c)
            self.assertEqual(codename[0][0], c)

    def test_print_examples(self):
        for i in range(100):
            print self.yehuda.generate()
