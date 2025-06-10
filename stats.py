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

def sort_char(chars):
     sorted = []
     for char in chars:
         if char.isalpha():
            sorted.append({"char" : char , "num" : chars[char]})

     def sort_on(dict):
          return dict["num"]
     
     sorted.sort(reverse=True, key=sort_on)
     return sorted