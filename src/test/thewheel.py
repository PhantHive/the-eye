import unittest
from ngrams import Ngram
from src.algotest.ngramTest import NGram as NgramTest


class TestNgram(unittest.TestCase):
    def setUp(self):
        # Set up the input sentence for the tests
        self.input_sentence = ["L'association", "IRIS", "est", "la", "meilleure"]

    def expected_output(self, input_sentence, n):
        # Define the expected output for the tests
        return Ngram(input_sentence, n).context()

    def test_ngrams(self):
        # Test ngrams() method for correct output
        self.assertEqual(self.expected_output(self.input_sentence, 3), NgramTest(self.input_sentence, 3).ngram())

    def test_ngrams_empty_sentence(self):
        # Test ngrams() method with empty sentence
        input_sentence = []
        self.assertEqual([[], []], NgramTest(input_sentence, 3).ngram())

    def test_ngrams_single_word_sentence(self):
        # Test ngrams() method with a single-word sentence
        input_sentence = ["word"]
        self.assertEqual([[], []], NgramTest(input_sentence, 3).ngram())

    def test_ngrams_short_sentence(self):
        # Test ngrams() method with a sentence that's too short for N=3
        input_sentence = ["short", "sentence"]
        self.assertEqual([[], []], NgramTest(input_sentence, 3).ngram())

    def test_ngrams_long_sentence(self):
        # Test ngrams() method with a sentence that's longer than N
        input_sentence = ["this", "is", "a", "long", "sentence", "with", "lots", "of", "words"]
        expected_output = self.expected_output(input_sentence, 3)
        self.assertEqual(expected_output, NgramTest(input_sentence, 3).ngram())



if __name__ == '__main__':
    unittest.main()
