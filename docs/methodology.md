# Methodology

This document outlines the six-step computational pipeline used for the analysis of
**HPAG1_0576** from *Helicobacter pylori*. Each step is implemented as a Jupyter
notebook (`notebooks/01`–`06`) and produces versioned outputs under `results/`.

## 1. Sequence Retrieval
- **Objective:** Obtain the primary amino-acid sequence.
- **Rationale:** Accurate sequence data is the foundation of all downstream analyses.
- **Tool:** UniProt API (`src/utils.py::fetch_uniprot_sequence`).
- **Output:** `data/raw/HPAG1_0576.fasta`.

## 2. Structure Prediction & Visualization
- **Objective:** Model the 3D structure of the protein.
- **Rationale:** Structural insight supports functional inference and identifies
  potential interaction surfaces.
- **Tool:** ColabFold (AlphaFold2-ptm), 6 recycles, Amber relaxation, MSA mode
  `mmseqs2_uniref_env`, 5 models ranked by pLDDT. Templates `2wcq` and `3vnc` were
  incorporated.
- **Output:** PDB models in `results/models/`; confidence plots (pLDDT, PAE, MSA
  coverage) in `results/figures/colabfold/`; per-model scores in
  `results/tables/colabfold/`. See `docs/colabfold_interpretation.md`.

## 3. Ramachandran Plot Analysis
- **Objective:** Validate the stereochemical quality of the predicted structure.
- **Rationale:** High-quality models must adhere to energetically favorable backbone
  dihedral angles (φ/ψ).
- **Tool:** MolProbity / Rama-Z.
- **Output:** Ramachandran plot and Z-scores at
  `results/figures/ramachandran_plot.pdf` (and `.kin`).

## 4. Active-Site & Binding-Pocket Detection
- **Objective:** Locate potential ligand-binding pockets.
- **Rationale:** Pockets indicate sites relevant to function and inhibitor design.
- **Tool:** CASTp 3.0 (CASTpFold).
- **Output:** Mouth/pocket tables and metrics under
  `results/tables/pocket_analysis/castp_results/`.

## 5. Physicochemical Analysis
- **Objective:** Determine molecular weight, charge, stability, and hydrophobicity.
- **Rationale:** Properties such as GRAVY and the aliphatic index inform solubility
  and thermal resilience; pI informs charge state.
- **Tool:** ExPASy ProtParam (via Biopython `ProtParam`).
- **Output:** Summary table at `results/tables/physicochemical/properties.csv`.

## 6. Domain & Conserved-Region Annotation
- **Objective:** Identify functional units, family signatures, and evolutionary
  conservation.
- **Rationale:** Conserved domains provide direct evidence of biological role (e.g.,
  the prokaryotic membrane lipoprotein lipid-attachment site) and cellular context.
- **Tool:** InterProScan (Pfam, Gene3D, ProSiteProfiles, Phobius, SignalP) and
  NCBI Conserved Domain Database (CDD) BLAST.
- **Output:** InterPro table at `results/tables/domain_analysis/iprscan_results.tsv`;
  CDD domain-annotation figure at `results/figures/cdd/HPAG1_0576_cdd_domain_annotation.svg`.

## Out of scope
Subcellular localization (PSORTb), virulence/antigenicity prediction
(VirulentPred, VaxiJen), and protein–protein interaction mapping (STRING) were
deliberately excluded from this repository and are **not** claimed as results.
