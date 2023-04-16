import time
import unittest
from ngrams import Ngram
from src.algotest.ngramTest import NGram as NgramTest


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

    def test_ngrams_repeated_words(self):
        # Test ngrams() method with repeated words
        input_sentence = ["This sentence has repeated words, this sentence has repeated words."]
        expected_output = self.expected_output(input_sentence, 4)
        self.assertEqual(expected_output, NgramTest(input_sentence, 4).ngram())

    def test_ngram_time_performance(self):
        # Test time performance of Ngram class
        start_time = time.perf_counter_ns()
        Ngram(self.input_sentence, 3).context()
        end_time = time.perf_counter_ns()
        print(f"IRIS Ngram class took {(end_time - start_time) / 1_000_000} ms to execute.")

    def test_ngram_test_time_performance(self):
        # Test time performance of NgramTest class
        start_time = time.perf_counter_ns()
        NgramTest(self.input_sentence, 3).ngram()
        end_time = time.perf_counter_ns()
        print(f"NgramTest class took {(end_time - start_time) / 1_000_000} ms to execute.")


if __name__ == '__main__':
    unittest.main()

