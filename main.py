def count_words(text):
 return len(text.split())

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print (f"Word count: {count_words(file_contents)}")

if __name__ == "__main__":
    main()