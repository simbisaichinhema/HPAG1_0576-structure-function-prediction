# Interpretation of ColabFold Results: HPAG1_0576

This document provides a scientific interpretation of the structural prediction
generated via ColabFold (AlphaFold2-ptm) for the protein HPAG1_0576.

## 1. Global Confidence Metrics

### Predicted Local Distance Difference Test (pLDDT)
- **Average pLDDT:** **83.1** (computed over the 192 residues of the top-ranked model).
- **Interpretation:** The model falls within the **"Confident"** range (70–90). The
  backbone fold is highly reliable and side-chain orientations are likely accurate for
  the majority of the protein.
- **Regional Variability:** Residues 1–24 (the N-terminal signal peptide) show low
  pLDDT (< 50), consistent with a disordered/cleavable leader. The mature domain
  (residues 25–192) is well-folded (pLDDT > 90).

### Predicted TM-score (pTM)
- **pTM:** **0.75**
- **Interpretation:** A pTM > 0.5 indicates a reliable global fold. A score of 0.75
  is strong, confirming that the overall topology is predicted with high confidence.
  The model is suitable for downstream tasks such as pocket detection and docking.

## 2. Multiple Sequence Alignment (MSA) & Templates
- **Templates Found:** `2wcq_A`, `3vnc_B`, `2wcq_B`.
- ColabFold combined these structural templates with a deep MSA. The presence of
  experimental templates from the PDB anchors the model to similar proteins and
  increases reliability.

## 3. Predicted Aligned Error (PAE)
- The PAE plot (`results/figures/colabfold/HPAG1_0576_f1e48_pae.png`) reports the
  uncertainty in the distance between pairs of residues.
- **Interpretation:** Dark blue blocks along the diagonal indicate well-defined
  regions whose relative residue distances are highly certain. Off-diagonal light
  regions would indicate flexible inter-domain linkages (minimal here, given a single
  compact domain).

## 4. Run Parameters & Optimization
- **Recycles:** 6 (increased from the default 3 to ensure structural convergence).
- **Relaxation:** The model was relaxed with the Amber force field to resolve steric
  clashes and improve stereochemistry, making it ready for pocket detection.
- **Models:** 5 AlphaFold2-ptm models, ranked by pLDDT; MSA mode `mmseqs2_uniref_env`.

## 5. Conclusion
The HPAG1_0576 model is of **high research grade**. The high pLDDT and pTM scores
provide a robust foundation for identifying functional residues and for the
lipoprotein interpretation developed in the domain analysis.

---
**Organized Files for Reference:**
- **Model:** `results/models/HPAG1_0576_colabfold_relaxed.pdb`
- **Visuals:** `results/figures/colabfold/`
- **Logs & citations:** `docs/colabfold/`
