'''Have the function StringChallenge(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"
Once your function is working, take the final output string and remove any characters (case-insensitive) from it that appear in your ChallengeToken.
If the new final string is empty, return the string EMPTY.

Your ChallengeToken: l0z8yp7e34'''

def StringChallenge(sen):
    
    sen=list(sen.split(" "))
    sen=[''.join(e for e in string if e.isalnum()) for string in sen]

    max_word=''
    
    for string in sen:
        if len(string)>len(max_word):
            max_word=string
  
    sen=max_word

  #time to remove the token from the the output
  
    token='l0z8yp7e34'
    sen=sen.lower()
    
    for char in token:
        sen=sen.replace(char, '')
        
    if len(sen)==0:
        return "EMPTY"
    else:
        return sen

        
# keep this function call here 
print(StringChallenge(input()))
