import sys

for line in sys.stdin:
    word, count = line.strip().split("\t")

    if word[0].lower() < 'n':
        print(f"0\t{word}\t{count}")
    else:
        print(f"1\t{word}\t{count}")