def cipher_encode(message, shift):
    """The function will take your original, decoded message and encode it using
    the shift value given

    Keyword_arguments:
    message -- user's message to be encoded
    shift -- the number of characters to shift the characters in the message
    forward

    Returns:
    message_output -- the message after it has been encoded
    """

    message_output = ''

    for char in message:
        if char.isupper():
            message_output += (chr(((((ord(char)) - 65) + shift) % 26) + 65))
        elif char.islower():
            message_output += (chr(((((ord(char)) - 97) + shift) % 26) + 97))
        elif char == ' ':
            message_output += ' '

    return message_output


def cipher_decode(message, shift):
    """The function will take your encoded message and decode it using
    the shift value given

    Keyword_arguments:
    message -- user's message to be decoded
    shift -- the number of characters to shift the characters in the message
    backwards back to their original value

    Returns:
    message_output -- the message after it has been decoded
    """

    message_output = ''

    for char in message:
        if char.isupper():
            message_output += (chr(((((ord(char)) - 65) - shift) % 26) + 65))
        elif char.islower():
            message_output += (chr(((((ord(char)) - 97) - shift) % 26) + 97))
        elif char == ' ':
            message_output += ' '

    return message_output


def cipher_decode_bruteforce(message):
    """The function will take your encoded message and decode it using
    a brute-force attack strategy. This function will print every possible
    message shift, each on its own line

    Keyword_arguments:
    message -- user's message to be decoded

    Returns:
    message_output -- every line of shifted message after it has been decoded
    """

    shift = 0
    message_output = ''

    while shift < 26:
        for char in message:
            if char.isupper():
                message_output += (chr(((((ord(char)) - 65) - shift) % 26) + 65))
            elif char.islower():
                message_output += (chr(((((ord(char)) - 97) - shift) % 26) + 97))
            elif char == ' ':
                message_output += ' '
        message_output += '\n'

        shift += 1
    return message_output
