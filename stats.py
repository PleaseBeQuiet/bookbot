def count_words(book):
     words = book.split()
     count = len(words)
     return count
    
def count_char(book):
     count = {}
     for char in book:
            if char.lower() in count:
               count[char.lower()] += 1
            else:
                 count[char.lower()] = 1
     return count