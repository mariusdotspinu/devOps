englishAlphabet = "abcdefghijklmnopqrstuvwxyz"


def removeDuplicates(input_list):

    list = []

    for i in input_list:
        if i not in list:
            list.append(i)


    returnedString = ''.join(list)

    return returnedString



def isPanagram(input_string):

    input_string = input_string.replace(' ','')
    input_string = input_string.lower()

    list_of_chars = list(input_string)

    list_of_chars.sort()

    returnedString = removeDuplicates(list_of_chars)

    if returnedString == englishAlphabet:
        return True
    else:
        return False


print isPanagram("The quick brown fox jumps over the lazy dog")