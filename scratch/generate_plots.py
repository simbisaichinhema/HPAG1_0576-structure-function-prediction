import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Add src to path
sys.path.append(os.getcwd())

from src.utils import parse_fasta, calculate_physicochemical_properties, get_amino_acid_composition

# Create directories if they don't exist
os.makedirs('results/figures', exist_ok=True)
os.makedirs('results/tables', exist_ok=True)

# 1. Parse Sequence
fasta_path = 'data/raw/HPAG1_0576.fasta'
record = parse_fasta(fasta_path)
sequence = record.seq

# 2. Calculate Properties
props = calculate_physicochemical_properties(sequence)
df_props = pd.DataFrame([props])
df_props.to_csv('results/tables/physicochemical_properties.csv', index=False)
print("Saved: results/tables/physicochemical_properties.csv")

# 3. Amino Acid Composition Plot
comp = get_amino_acid_composition(sequence)
plt.figure(figsize=(12, 6))
# Sort by residue name for consistent plotting
sorted_comp = dict(sorted(comp.items()))
sns.barplot(x=list(sorted_comp.keys()), y=list(sorted_comp.values()), palette='viridis')
plt.title("Amino Acid Composition of HPAG1_0576", fontsize=14)
plt.xlabel("Residue", fontsize=12)
plt.ylabel("Percentage (%)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("results/figures/aa_composition.png", dpi=300, bbox_inches='tight')
print("Saved: results/figures/aa_composition.png")

# 4. Save JSON for notebook display
with open('results/tables/aa_composition.json', 'w') as f:
    import json
    json.dump(comp, f, indent=4)
