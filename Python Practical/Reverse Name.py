def reverse(S):
    str=" "
    for i in S:
        str=i + str
    return str
S ="Alister"
print(reverse(S))
