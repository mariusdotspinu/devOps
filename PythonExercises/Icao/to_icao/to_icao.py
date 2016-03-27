#!/usr/bin/env python
# *-* coding: UTF-8 *-*

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao():

    try:
        my_input_file = open("input_icao", "r")
        strings = my_input_file.read()
        my_input_file.close()
    except IOError:
        print "Error encountered"
        return

    final_list = []

    for line in strings.splitlines():
        for char in line:
            if char in ICAO:
                final_list.append(ICAO.get(char))
                final_list.append(' ')
        final_list.append('\n')

    returned_text = ''.join(final_list)

    try:
        my_output_file = open("to_icao_output.txt", "w")
        my_output_file.write(returned_text)
        my_output_file.close()
    except IOError:
        print "Could not open output file"


if __name__ == "__main__":
    icao()
