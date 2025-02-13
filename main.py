def count_words(text):
 return len(text.split())

def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
      if char in char_count:
         char_count[char] += 1
      else:
         char_count[char] = 1

    return char_count

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print (f"Word count: {count_words(file_contents)}")
    print ("Character count:", count_characters(file_contents))
if __name__ == "__main__":
    main()