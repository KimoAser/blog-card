def find_anagrams(word, candidates):
    listing = []
    for i in candidates:
        if word.lower() == i.lower():
            continue
        word_lowered = word.lower()
        cand_lowered = i.lower()
        if sorted(word_lowered) == sorted(cand_lowered):
            listing.append(i)
    return listing
