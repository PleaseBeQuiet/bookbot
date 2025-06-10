from stats import count_words, count_char, sort_char

def get_book_text(book):
    #print("get_book_text called")
    with open(book) as f:
        book_contents = f.read()
        return book_contents
            
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_count = count_char(text)
    sorted = sort_char(char_count)

    print("============ BOOKBOT ============")
    print(f"analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    tick = 0
    for i in sorted:
        print(f"{sorted[tick]["char"]}: {sorted[tick]["num"]}")
        tick += 1
    print("============= END ===============")

main()