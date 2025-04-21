import random
import pandas as pd

def generate_dna_sequence(length):
    return ''.join(random.choices("ACGT", k=length))

def generate_dataset(n_samples=10000, seq_length=200, pathogen_ratio=0.5):
    data = []
    n_pathogens = int(n_samples * pathogen_ratio)
    n_benign = n_samples - n_pathogens

    for _ in range(n_pathogens):
        # Slightly more complex/GC-rich pattern for mock pathogen
        seq = generate_dna_sequence(seq_length)
        seq = seq.replace('A', 'G', 3)  # introduce bias
        data.append({"sequence": seq, "label": "pathogen"})

    for _ in range(n_benign):
        seq = generate_dna_sequence(seq_length)
        seq = seq.replace('G', 'A', 3)  # introduce different bias
        data.append({"sequence": seq, "label": "benign"})

    random.shuffle(data)
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_dataset(n_samples=100000, seq_length=200, pathogen_ratio=0.5)
    df.to_csv("data/generated_sequences.csv", index=False)
    print("✅ Generated data saved to data/generated_sequences.csv")

