#!/usr/bin/env python
# *-* coding: UTF-8 *-*

from __future__ import print_function


def decrypt_message(message):

    list_chars_of_message = list(message)

    key = ord(list_chars_of_message[0]) - ord('a')

    returned_list = []

    for i in list_chars_of_message:

        if ord(i) < 97 or \
                        ord(i) > 122:
            returned_list.append(i)
        else:

            if ord(i) - key >= 97 and \
                                    ord(i) - key <= 122:
                returned_list.append(chr(ord(i) - key))

            elif ord(i) - key < 97:

                until_last_letter = ord(i) - ord('a')

                decrypted_letter = chr(ord('z') - key + until_last_letter + 1)

                returned_list.append(decrypted_letter)

    returned_message = ''.join(returned_list)

    print(returned_message)


def main():
    """ Main function docstring """
    try:
        my_file = open("mesaje.secret", "r")
        messages = my_file.read()
        my_file.close()
    except IOError:
        print("Could not get files.")
        return

    for message in messages.splitlines():
        decrypt_message(message)


if __name__ == "__main__":
    main()
