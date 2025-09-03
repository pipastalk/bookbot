def get_num_words(text):
    words = text.split()
    return len(words)
def character_count(text):
    character_count = {}
    unique_characters = set(text.lower())
    for character in unique_characters:
        character_count[character] = text.lower().count(character)
    return character_count


def sort_dictionary(d):
    def sort_on(items):
        type(items)
        return items[1]
    sorted_dict = dict(sorted(d.items(), key=sort_on, reverse=True))
    return sorted_dict