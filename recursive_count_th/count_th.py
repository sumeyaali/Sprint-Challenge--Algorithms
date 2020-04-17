'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.


1. look at each index of the string ([0,1] because th have to be together): if th is in the string, call count_th and
increment counter 
else return 0 
'''
def count_th(word):
    th_string = "th"
    #base case, word has to have at least 2 letters to have "th" in it
    if len(word) < 2:
        return 0
    if th_string == word[0:2]:
        return 1 + count_th(word[2:])
    else:
        return count_th(word[2:])

print(count_th('thoughthtfulth'))

