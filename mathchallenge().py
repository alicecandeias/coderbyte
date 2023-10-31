'''Have the function MathChallenge(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears.
Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string.
Another example: if str is "abababababab" then your program should return ababab because it is the longest substring.
If the input string contains only a single character, your program should return the string -1'''

def MathChallenge(strParam):

    if len(set(strParam)) == 1:
            return -1

    longest=''
    substring=''

    for i in range (0,len(strParam)//2):
        substring+=strParam[i]
        if substring*(len(strParam)//len(substring)) == strParam:
            longest=substring

    if longest:
        return longest
    else:
        return -1
