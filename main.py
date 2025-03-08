from stats import word_count, character_count, sort_character_count, sort_on
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = sys.argv[1]
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
