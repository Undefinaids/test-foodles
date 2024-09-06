"""Core module for the foodles package."""

from collections import Counter


def word_frequency(sentence: str, n: int) -> list[tuple[str, int]]:
    """
    Calculate the frequency of words in a given sentence and return the top `n` words.
    Args:
        sentence (str): The input sentence.
        n (int): The number of top words to return.
    Returns:
        list[tuple[str, int]]: A list of tuples containing the word and its frequency, sorted by frequency (descending) and alphabetically (ascending) in case of ties.
    Raises:
        ValueError: If `n` is less than or equal to 0.
    Example:
        >>> word_frequency("I love to eat pizza and pasta", 3)
        [('and', 1), ('eat', 1), ('I', 1)]
    """
    if n <= 0:
        raise ValueError("n must be a positive value greater than 0")

    # Split the sentence into words
    words = sentence.split()

    # Count the frequency of each word
    word_count = Counter(words)

    # Sort the words by frequency (descending) and alphabetically (ascending) in case of ties
    # I lowercased the string in the sorted function because in ASCII, the uppercase letters come before the lowercase letters
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0].lower()))

    # Return the top `n` words
    return sorted_words[:n]
