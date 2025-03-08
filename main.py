from stats import word_count, character_count, sort_character_count, sort_on

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	filepath = "./books/frankenstein.txt"
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}")
	text = get_book_text(filepath)
	num_words = word_count(text)
	characters = character_count(text)
	sorted_count = sort_character_count(characters)
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for dict in sorted_count:
		print(f"{dict["character"]}: {dict["count"]}")
	print("============= END ===============")
	return

main()
