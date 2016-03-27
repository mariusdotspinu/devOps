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


def from_icao(message):


    try:
        my_file = open(message)
        strings = my_file.read()
        my_file.close()
    except IOError:
        print "Error encountered"
        return

    final_list_of_lines = []

    for line in strings.splitlines():
        processed_list = []

        if line[0] in ICAO:
            processed_list.append(line[0])

        for i, obj in enumerate(line):
            if obj == ' ':
                if line[i + 1] in ICAO and line[i + 1]:
                    processed_list.append(line[i + 1])

        processed_list.append('\n')
        current_row = ''.join(processed_list)

        final_list_of_lines.append(current_row)

    try:
        output_file = open("output.txt", "r+")
        message = ''.join(final_list_of_lines)
        output_file.write(message)
        output_file.close()
    except IOError:
        print "Error encountered"
        return


if __name__ == "__main__":
    from_icao("mesaj.icao")
