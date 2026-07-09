import os
import requests
from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd

def fetch_uniprot_sequence(uniprot_id, output_path):
    """
    Fetches a protein sequence from UniProt and saves it as a FASTA file.
    """
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(response.text)
        return True
    else:
        print(f"Error fetching sequence: {response.status_code}")
        return False

def parse_fasta(file_path):
    """
    Parses a FASTA file and returns the record.
    """
    return list(SeqIO.parse(file_path, "fasta"))[0]

def calculate_physicochemical_properties(sequence):
    """
    Calculates basic physicochemical properties of a protein sequence.
    """
    analysis = ProtParam.ProteinAnalysis(str(sequence))
    properties = {
        "Molecular Weight": analysis.molecular_weight(),
        "Isoelectric Point": analysis.isoelectric_point(),
        "GRAVY": analysis.gravy(),
        "Instability Index": analysis.instability_index(),
        "Aromaticity": analysis.aromaticity()
    }
    return properties

def get_amino_acid_composition(sequence):
    """
    Returns the amino acid composition as a dictionary.
    """
    analysis = ProtParam.ProteinAnalysis(str(sequence))
    return analysis.get_amino_acids_percent()
