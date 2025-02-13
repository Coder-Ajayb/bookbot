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

def print_report(filename, word_count, char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    words = count_words(file_contents)
    char_counts = count_characters(file_contents)
    print_report(path_to_file, words, char_counts)
    

if __name__ == "__main__":
    main()