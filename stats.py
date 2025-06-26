def count_words(text):
    words_list =  text.split()
    return len(words_list)

def get_number_chars(text):
    text = text.lower()
    characters = {}
    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters


def sort_by_num(items):
    return items["num"]
   
def sort_characters_dict(chars):
    list_dict_chars = []
    for c in chars:
        char_dict = {}
        list_dict_chars.append({'char':c,'num': chars[c]})
    list_dict_chars.sort(reverse=True,key=sort_by_num)
    return list_dict_chars
