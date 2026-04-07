# 2. File Handling: Write a script that reads a large text file, counts the frequency of each word, and writes the results to a new file.

import os

def count_word_frequency(input_file, output_file):
    word_count = {}

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:   # Efficient for large files
                words = line.lower().split()

                for word in words:
                    word = word.strip(".,!?\"'()[]{}")  # remove punctuation

                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

        # Write output
        with open(output_file, "w", encoding="utf-8") as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word} : {count}\n")

        print(f" Word frequency written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(" Input file not found. Please check the file name.")

def main():
    input_file = "input.txt"     
    output_file = "output.txt"   

    count_word_frequency(input_file, output_file)

if __name__ == "__main__":
    main()