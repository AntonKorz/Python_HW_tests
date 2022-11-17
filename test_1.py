from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    >>> encode('A')
    '.-'
    >>> encode('ABDCDGSFWRYHSDHFK') # doctest: +ELLIPSIS
    '.- -... -..... .... ..-. -.-'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('AAAAAAAAAAAAAA')
    '.- .- .- .- .- .- .-
    .- .- .- .- .- .- .-'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == "__main__":
    import doctest

    doctest.testmod()