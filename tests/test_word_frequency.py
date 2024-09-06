import pytest

from foodles import word_frequency


def test_word_frequency_basic_input():
    sentence = "I love to eat pizza and pasta"
    n = 3
    expected_output = [("and", 1), ("eat", 1), ("I", 1)]
    assert word_frequency(sentence, n) == expected_output


def test_word_frequency_empty_sentence():
    sentence = ""
    n = 5
    expected_output = []
    assert word_frequency(sentence, n) == expected_output


def test_word_frequency_repeated_words():
    sentence = "apple apple orange orange orange"
    n = 2
    expected_output = [("orange", 3), ("apple", 2)]
    assert word_frequency(sentence, n) == expected_output


def test_word_frequency_special_characters():
    sentence = "Hello, world! How are you?"
    n = 4
    expected_output = [("are", 1), ("Hello,", 1), ("How", 1), ("world!", 1)]
    assert word_frequency(sentence, n) == expected_output


def test_word_frequency_n_zero():
    sentence = "This is a test sentence"
    n = 0
    with pytest.raises(ValueError):
        word_frequency(sentence, n)
