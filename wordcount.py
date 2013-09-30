# lower everything
# replace double hypen with space
# split everything on space
# get rid of punctuation

from sys import argv

script, filename = argv

text = open(filename)

filetext = text.read()
text.close()

def clean_text(any_text):
    lower_case = any_text.lower()
    replace_hyphen = lower_case.replace("--", " ")
    split_list = replace_hyphen.split()
    left_side_clean = []
    for item in split_list:
        left_side_clean.append(item.lstrip("\'\""))
    print left_side_clean
        


clean_text(filetext)




"""
no_punctuation = ""
for char in lower_case:
    if 97 <= ord(char) <= 122 or ord(char) == 32:
        no_punctuation += char



list_of_words = no_punctuation.split()

d = {}
for word in list_of_words:
    if d.get(word) == None:
        d[word] = list_of_words.count(word)
        #print word, d[word]



print d
print d.items()
"""







"""
# print filetext


list_of_split_words = lower_case.split()

for item in list_of_split_words:
    item.strip(",.:;?/'\"[]{}><!@#$%^&-_*()")

print list_of_split_words

"""
