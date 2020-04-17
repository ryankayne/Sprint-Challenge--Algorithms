'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    sub = "th"
    
    if word.find(sub) != -1:
        count += 1
        return 1 + count_th(word[0:len(word) -1])
    else:
        return count

print(count_th("thingth"))

# new_str = test_str.replace('e', '') 

# def count_th(word):
#     count = 0
#     sub = "th"
#     if word.find(sub) != -1:
#         count + 1
#         return count_th(word)
#     else:
#         return count

# print(count_th("th"))

# def count_th(word):
#     count = 0
#     sub = "th"
#     if word.count(sub):
#         count + 1
#         return count_th(word)
#     else:
#         return count

# print(count_th("th"))

# def count_th(word):
#     length = len(word)

#     if (length == 0):
#         return 0
#     else:
#         if (word[0:length] == "th"):
#             return count_th(word[length - 1])

# print(count_th("th"))