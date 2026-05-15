print("37 Alister Quinny")
import string
def is_pangram(sentence):
    alphabet=set(string.ascii_lowercase)
    sentence_letters=set(sentence.lower())
    return alphabet <= sentence_letters
sentence="The quick brown foo jumps over the lazy dog"
result=is_pangram(sentence)

if result:
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")
