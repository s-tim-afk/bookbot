def word_count(text):
        words = text.split()
        return len(words)

def character_count(text):
	characters = {}
	for character in text:
		char = character.lower()
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	return characters

def sort_on(dict):
	return dict["count"]

def sort_character_count(dict):
	sorted_characters = []
	for key in dict:
		character = key
		count = dict[key]
		if key.isalpha() == True:
			sorted_characters.append({"character": character, "count": count})
	sorted_characters.sort(reverse=True, key=sort_on)
	return sorted_characters
