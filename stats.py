# splits the text into a list of individual words
# then returns the size of the list
def get_word_count(text):
	return len(text.split())

# Iterates through the entire text that has been converted to lower case
# does a character count for each character
def get_character_count(text):
	character_count = {}	
	for letter in text.lower():
		if letter in character_count:
			character_count[letter] += 1
		else:
			character_count[letter] = 1
	return character_count

def sorted_list(char_dict):
	
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
	
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list