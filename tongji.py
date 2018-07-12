import string

lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()
print(words)

def function_Count(filename):
    with open(filename,'r') as text:
        words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
        words_index = set(words)
        counts_dict = {index:words.count(index) for index in words_index}
        for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
            print('{}-{} times'.format(word, counts_dict[word]))
        #print(words)
        # for word in words:
        #     print('{}-{} times'.format(word,words.count(word)))


function_Count('F:/code/python/Walden.txt')