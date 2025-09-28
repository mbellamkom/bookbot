import stats
import sys

#CLI interface for bookbot
#print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
try:
    with open (book_path) as f:
        file_contents = f.read()
except FileNotFoundError:
    #if user didn't add the filepath
    if not book_path.startswith("books/") and book_path.endswith(".txt"):
        print("Error: Book path needs to be spcified")
    else:
        print(f"Error: The file was not found at: {book_path}")
    sys.exit(1)

""" #ask the user to pick a book
while True:
 choose_book = "frankenstein.txt" #input("Enter a book name. Ex. Frankenstein.txt")
 book_path=f"books/{choose_book}"   
 try:
    with open (book_path) as f:
        file_contents = f.read()
        break
 except FileNotFoundError:
        print("The file was not found. Please try again.") """



word_count = stats.get_num_words(file_contents)
character_counts_dict = stats.counting_characters(file_contents)
character_dictionary =  stats.character_dict(character_counts_dict)
final_dict_list = stats.dict_grouping(character_dictionary)

    
#report generation
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print(f"----------- Word Count ----------")
print(f"Found {word_count} total words")
print(f"--------- Character Count -------")
#format final character count list
for item in final_dict_list:
    print(f"{item['char']}: {item['count']}")
print(f"============= END ===============")
