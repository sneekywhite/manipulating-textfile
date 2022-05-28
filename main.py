# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from re import I


def read_file_content(filename):
    with open(filename) as f:
        for line in f:
            return line
    
    



def count_words():
    text = read_file_content("./story.txt")
    texts = text.split()
    count = {}

    for i in texts:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key in list(count.keys()):
        print(key,":", count[key])
    return (count_words)


print(count_words())