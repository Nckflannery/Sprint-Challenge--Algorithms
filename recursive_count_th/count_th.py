'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case
    if len(word) < 2:
        return 0
    # If first two letters of word are 'th'
    if word[:2] == 'th':
        # Recursion, and +1 to return
        return count_th(word[2:]) + 1
    # If first two letters not 'th' move to next letter
    else:
        return count_th(word[1:])

