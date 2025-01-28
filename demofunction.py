# Counting words using regex, explain this code

def count_words(s: str) -> int:
    import re
    words = re.findall(r'\b\w+\b', s)
    word_count = len(words)
    return word_count


s = "Python: easy, powerful, and flexible!"
print(count_words(s))
