#!/usr/bin/python


#check if the input string is equal to the reversed self
def checkIfPalindrom (input_string):

    input_string = input_string.replace(' ','') #eliminate whitespaces

    input_string = input_string.lower() #make the string lowercase

    normal_string = input_string

    my_list = list(input_string) #converting string to list of characters

    my_list.reverse() #reversing the list

    reversed_string = ''.join(my_list) #converting list back to string

    if normal_string == reversed_string:
        return True
    else:
        return False


#check if first string s1 begins and terminates with second string s2
def start_end (s1,s2):

     if len(s1) < len(s2): # if length of first string is less than the second return false
         return False

     len_s2 = len(s2)

     list_chars_s1 = list(s1)

     list_chars_s2 = list(s2) # creating the lists

     len_s2_reached = 0

     for i in range(len(list_chars_s1)): # we check if the first elements of the first equals the elements of the second
        if i < len(list_chars_s2):
         if list_chars_s1[i] == list_chars_s2[i]:
             len_s2_reached = len_s2_reached + 1

         if len_s2_reached == len_s2: #to know where to stop
             break
     else:
         return False

     j = len_s2 - 1

     len_s2_reached = 0

     for i in range(len(list_chars_s1))[::-1]: #same , but reverse
        if i > j and j >=0:
         if list_chars_s1[i] == list_chars_s2[j]:
             len_s2_reached = len_s2_reached + 1

         if len_s2_reached == len_s2:
             break
        j -= 1
     else:
         return False

     return True


#check if two strings has the same number of letters and the same letters
def checkIfAnagrams (s1,s2):

    list_s1 = list(s1)
    list_s2 = list(s2) #creating lists

    list_s1.sort()
    list_s2.sort() # we sort them alphabetically , so we can compare them

    if list_s1 == list_s2:
        return True
    else:
        return False


#check if string s2 is contained by string s1
def strinside (s1,s2):

    if len(s1) < len(s2):
        return False

    list_s1 = list(s1)
    list_s2 = list(s2)

    contained = False

    number_of_same_chars = 0

    j = 0

    for i in range(len(s1)):
        if (list_s1[i] == list_s2[j]):
            number_of_same_chars += 1
            j += 1
        else:
            number_of_same_chars = 0
            j = 0

        if number_of_same_chars == len(s2):
            contained = True
            break

    if contained == True:
        return True
    else:
        return False


print checkIfPalindrom("cojoc")
print start_end("abadecba","a")
print checkIfAnagrams("caer","rac")
print strinside("hqweqwrqwhelloworld","helloworld")
