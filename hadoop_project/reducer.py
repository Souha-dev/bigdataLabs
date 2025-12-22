#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # ligne mal formée, on l’ignore
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# dernier mot
if current_word is not None:
    print(f"{current_word}\t{current_count}")
