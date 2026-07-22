import sys

current_word = None
current_count = 0

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) == 3:
        _, word, count = parts
    else:
        word, count = parts

    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word:
    print(f"{current_word}\t{current_count}")