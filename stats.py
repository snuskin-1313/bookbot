def count_chars(text):
    chars = {}
    lower_text = text.lower()

    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars  

def count_words(text):
    new_text = text.split()
    return len(new_text)

def get_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# read from count_chars()
def sort_chars(chars):
    # create a list of dictionaries
    ch_list = []

    for ch in chars:
        c = chars[ch]
        new_dict = {"char": ch, "count": c}
        ch_list.append(new_dict)

    ch_list.sort(reverse=True, key=sort_on)

    return ch_list

def sort_on(dict):
    return dict["count"]