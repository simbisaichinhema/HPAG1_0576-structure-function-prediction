# Computational Structural & Functional Analysis of HPAG1_0576 (*Helicobacter pylori*)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

A reproducible computational-biology pipeline that characterizes **HPAG1_0576**, an
unannotated protein-coding gene from *Helicobacter pylori* strain HPAG1. The analysis
combines *ab initio* structure prediction, stereochemical validation, pocket
detection, physicochemical profiling, and domain/conserved-region annotation to
propose a biological role for the protein.

---

## Biological context

*Helicobacter pylori* is a gastric pathogen implicated in peptic ulcer disease,
gastritis, and gastric cancer. HPAG1_0576 is a short (192-aa) protein of unknown
function. Computational evidence gathered here indicates it is a **secreted
lipoprotein**: it carries an N-terminal signal peptide and a canonical prokaryotic
membrane **lipoprotein lipid-attachment site**, and its mature domain is predicted to
reside outside the cytoplasm. This repo documents the evidence behind that
interpretation and provides the pipeline to reproduce it.

---

## Pipeline & key results

The pipeline is implemented as six Jupyter notebooks (`notebooks/01`–`06`), each
producing versioned artifacts under `results/`.

| # | Analysis | Tool(s) | Headline result |
|---|----------|---------|-----------------|
| 1 | Sequence retrieval | UniProt API | 192-aa sequence cached at `data/raw/HPAG1_0576.fasta` |
| 2 | Structure prediction | ColabFold (AlphaFold2-ptm) | **mean pLDDT 83.1**, **pTM 0.75**, 6 recycles, templates 2wcq/3vnc |
| 3 | Ramachandran validation | MolProbity / Rama-Z | Stereochemical plot at `results/figures/ramachandran_plot.pdf` |
| 4 | Active-site / pocket detection | CASTp 3.0 | **14 surface pockets**; largest mouths 53.6 Å² & 41.6 Å² (SA) |
| 5 | Physicochemical profiling | ExPASy ProtParam | MW **21 851 Da**, pI **8.36**, instability **49.85**, GRAVY **−0.220** |
| 6 | Domain & conserved-region annotation | InterProScan + NCBI CDD | Signal peptide + **lipoprotein** lipobox (PS51257); NON_CYTOPLASMIC_DOMAIN 25–192 |

### Structure (Step 2)
ColabFold produced five AlphaFold2-ptm models ranked by pLDDT. The top model has a
mean pLDDT of **83.1** (Confident) with a **pTM of 0.75**, indicating a reliable
global fold suitable for downstream pocket and functional analysis. Residues 1–24
(N-terminal signal peptide) are low-confidence/disordered, while the mature domain
(residues 25–192) is well-folded (pLDDT > 90). Structural templates
`2wcq_A`, `3vnc_B`, and `2wcq_B` were incorporated. Full interpretation in
[`docs/colabfold_interpretation.md`](docs/colabfold_interpretation.md).

### Physicochemistry (Step 5)
Computed with Biopython `ProtParam` over the 192-residue sequence:

| Property | Value |
|----------|-------|
| Length | 192 aa |
| Molecular weight | 21 851.32 Da |
| Isoelectric point (pI) | 8.36 |
| Instability index | 49.85 |
| Aliphatic index | 95.94 |
| GRAVY | −0.220 |

### Domain annotation (Step 6)
InterProScan (and NCBI CDD) identify:
- **Gene3D** `G3DSA:3.10.129.140` — globular domain, residues 34–192
- **Signal peptide** (Phobius 1–24; SignalP-TM 1–33)
- **Prokaryotic membrane lipoprotein lipid attachment site** (ProSiteProfiles `PS51257`, 1–25) — the *lipobox*
- **NON_CYTOPLASMIC_DOMAIN** (Phobius, 25–192) — predicts an extracellular / outer-membrane location

Together these classify HPAG1_0576 as a **lipoprotein**, consistent with export to the
bacterial cell envelope.

---

## Repository structure

```text
.
├── data/
│   ├── raw/                       # Curated inputs (committed)
│   │   ├── HPAG1_0576.fasta       #   UniProt sequence
│   │   └── msa/                   #   ColabFold MSA (.a3m)
│   └── processed/                 # Intermediate data (gitignored)
├── notebooks/                     # Analysis pipeline 01–06
├── src/utils.py                   # Reusable fetch / parse / property helpers
├── scratch/generate_plots.py      # Auxiliary plotting helper
├── results/
│   ├── figures/
│   │   ├── colabfold/             # pLDDT, PAE, MSA coverage plots
│   │   ├── cdd/                   # NCBI CDD domain-annotation SVG
│   │   └── ramachandran_plot.pdf
│   ├── tables/
│   │   ├── physicochemical/       # properties.csv
│   │   ├── domain_analysis/       # iprscan_results.tsv
│   │   ├── pocket_analysis/       # CASTp outputs
│   │   └── colabfold/             # scores, PAE, config
│   └── models/                    # Relaxed / unrelaxed PDB + all_ranks/
├── docs/
│   ├── methodology.md
│   ├── colabfold_interpretation.md
│   └── colabfold/                 # ColabFold run logs / citations
├── reports/{draft,final}/         # Reserved for written reports
├── requirements.txt
├── LICENSE                        # CC BY 4.0
├── CITATION.cff
└── README.md
```

---

## Installation & reproducibility

Requires **Python 3.9+**.

```bash
git clone <repo-url>
cd computational-analysis-HPAG1_0576

python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook                   # run notebooks 01 → 06 in order
```

Notebooks are provided as clean source (no embedded outputs). Running them in
sequence regenerates every artifact under `results/`. The curated result files are
already committed so the repository is browsable without execution.

---

## Scope & limitations

This repository covers the **six analyses listed above**. The following were scoped
out and are **not** included (no results are claimed for them):
- Subcellular localization (PSORTb)
- Virulence / antigenicity prediction (VirulentPred, VaxiJen)
- Protein–protein interaction mapping (STRING)

Structure prediction is *in silico* (ColabFold/AlphaFold2); experimental validation
(X-ray, NMR, or cryo-EM) would be required to confirm the model. Domain predictions
are computational and should be interpreted accordingly.

---

## Data availability

- Input sequence: `data/raw/HPAG1_0576.fasta` (UniProt-derived).
- All intermediate and final results are committed under `results/`.
- External databases used: UniProt, InterPro, NCBI CDD, CASTp, ColabFold/AlphaFold.

---

## How to cite

If you use this analysis, please cite the repository and the underlying tools:

```bibtex
@software{hpag1_0576_analysis,
  author = {Simbisai Chinhema},
  title  = {Computational Structural and Functional Analysis of HPAG1_0576 (Helicobacter pylori)},
  year   = {2026},
  license = {CC BY 4.0},
  url    = {https://github.com/simbisaichinhema/HPAG1_0576-structure-function-prediction}
}
```

See [`CITATION.cff`](CITATION.cff) for the machine-readable version. Key upstream
citations (ColabFold, AlphaFold, InterPro, CASTp, NCBI CDD) are collected in
[`docs/colabfold/cite.bibtex`](docs/colabfold/cite.bibtex).

---

## License

Content, code, and results are released under **[CC BY 4.0](LICENSE)**. The
underlying protein/structure data originate from public databases and remain subject
to their respective terms.

## Acknowledgements

- UniProt for sequence data
- The ColabFold / AlphaFold teams for structure prediction
- InterPro & the NCBI CDD for domain annotation
- CASTp for pocket analysis
- ExPASy ProtParam (Biopython) for physicochemical properties
