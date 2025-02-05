#Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

my_string = (input())
my_string = ''.join(i if i.isalnum() else ' ' for i in my_string)
words = my_string.split()
hashtag = '#' + ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)