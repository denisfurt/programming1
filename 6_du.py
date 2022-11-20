raw_sentence = input()
w_num = int(input())
words = list(map(str, raw_sentence.split()))
#
#def print_w_chars(words, w):
#    n = len(words)
#    raw = ''
#    raw_len = 0
#    word_count = 0
#    i = 0
#
#    while i < n:
#        raw_len = raw_len + len(words[i]) + 1
#
#        print("-------------------------------")
#        print("I: " + str(i) + "  " + "Raw_len: " + str(raw_len))
#        print("Raw: " + raw + " " + " n:" + str(n))
#        print("Word count: " + str(word_count))
#        print("Current word: " + str(words[i]))
#        print("-------------------------------")
#
#        if raw_len >= w + 1:
#            if word_count == 0:
#                print(words[i])
#            else:
#                i = i - 1
#                print(raw)
#            raw = ''
#            raw_len = 0
#            word_count = 0
#        else:
#            if i == n - 1:
#                raw = raw + " " + words[i]
#                print(raw)
#            elif word_count == 0:
#                raw = words[i]
#            else:
#                raw = raw + " " + words[i]
#            word_count = word_count + 1
#        i = i + 1
#
#
#

def sort_words_chunks(words, chunk_max_size):
    words_len = len(words)
    chunks = []
    curr_chunk = []
    chunk_size = 0

    for i in range(0, words_len - 1):
        print("-------------------------------")
        print("words_len: " + str(words_len))
        print("I: " + str(i) + "  " + "curr_chunk: ")
        print(curr_chunk)
        print("-------------------------------")
        if chunk_size != 0:
            estimated_chunk_size = chunk_size + 1 + len(words[i])
        else:
            estimated_chunk_size = len(words[i])

        if estimated_chunk_size >= chunk_max_size and chunk_size != 0:
            chunks.append(curr_chunk)
            chunk_size = 0
            curr_chunk = []
            curr_chunk.append(words[i])
        else:
            chunk_size = estimated_chunk_size
            curr_chunk.append(words[i])

    return chunks



print(sort_words_chunks(words, w_num))
#print_w_chars(words, w_num)
