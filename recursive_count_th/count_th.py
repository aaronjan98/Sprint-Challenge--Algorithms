'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# initialize count
count = 0

def count_th(word):
    '''
    # first pass solution, but without recursion
    th_count = word.count('th')
    return th_count
    '''
    global count

    # base case
    if "th" in word:
        count += 1
        del_index = word.find('th')
        print('COUNT:', count)
        word = word[del_index+1:]
        print(word)
        # recursive call
        count_th(word)
    else:
        global r_count
        r_count = count
        count = 0
        print('r:', r_count)

    return r_count

# count_th("thhtthht")