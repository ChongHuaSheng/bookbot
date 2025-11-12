def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    my_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in my_dict:
            my_dict[f"{lower_char}"] = 1
            continue
        my_dict[f"{lower_char}"] += 1
    return my_dict
