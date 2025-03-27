def is_anagram(word_a, word_b):
    word_a = word_a.replace(" ", "").lower()
    word_b = word_b.replace(" ", "").lower()
    if len(word_a) != len(word_b):
        return False
    return sorted(word_a) == sorted(word_b)

def anagrame(cuvant1, cuvant2):
    cuvant1 = cuvant1.replace(" ", "").lower()
    cuvant2 = cuvant2.replace(" ", "").lower()
    if len(cuvant1) != len(cuvant2):
        return False
    return sorted(cuvant1) == sorted(cuvant2)

print(is_anagram("lisen", "silent"))