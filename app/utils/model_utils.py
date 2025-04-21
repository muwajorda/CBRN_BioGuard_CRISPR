import random

def classify_sequence(seq):
    if "AGAGCTAGAA" in seq or "GTTTTAGAGCTAGAAATAGC" in seq:
        return "biothreat", "Biological"
    elif "CAGTCC" in seq or "TTCGGA" in seq:
        return "chem-threat", "Chemical"
    elif "TATATA" in seq or "GCGCGC" in seq:
        return "radio-threat", "Radiological"
    elif "AATTCCGG" in seq or "CCGGTTAA" in seq:
        return "nuke-threat", "Nuclear"
    else:
        return random.choice([("non-threat", "Biological"), ("non-threat", "Chemical"),
                              ("non-threat", "Radiological"), ("non-threat", "Nuclear")])

