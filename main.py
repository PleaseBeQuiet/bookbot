from stats import count_words, count_char

def get_book_text(book):
    #print("get_book_text called")
    with open(book) as f:
        book_contents = f.read()
        return book_contents
            
def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = count_words(text)
    print(f"{num_words} words found in the document")

    char_count = count_char(text)
    print(char_count)

main()