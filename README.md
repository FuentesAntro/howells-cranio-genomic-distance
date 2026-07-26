# Howells Cranio-Genomic Distance

**Morphometric variability of 2,524 crania from 28 populations worldwide and its correlation with genomic distance.**

![R](https://img.shields.io/badge/R-%3E%3D%204.2-blue)
![Data](https://img.shields.io/badge/data-2,524%20crania-green)
![Populations](https://img.shields.io/badge/populations-28-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

### Overview

This repository presents a quantitative analysis of human cranial variation using the classic **Howells Craniometric Dataset**. The goal is to (1) characterize global morphometric variability and (2) test to what extent cranial morphology predicts neutral genomic differentiation.

This project serves as a reproducible workflow for craniometric analysis and as a foundation for a future cranio-genomic distance paper.

> **Dataset in use:** `data/raw/howells_raw.csv` - 2,524 individuals x 82 measurements

### 1. Dataset Provenance

*   **Original collection:** W.W. Howells (Harvard University, Peabody Museum of Archaeology and Ethnology), 1960s-1970s. Direct caliper measurements on skeletal collections worldwide.
*   **Populations (28):** NORSE, ZALAV, BERG, EGYPT, TEITA, DOGON, ZULU, BUSHMAN, SAN, AUSTRALIA, TOLAI, MOKAPU, MOKPU, GUAM, ATAYAL, PHILIP, ANYANG, HAINAN, N-JAPAN, S-JAPAN, AINU, BURIAT, ESKIMO, etc.
*   **Variables:** 57-82 craniometric measurements following Martin & Howells. e.g., GOL (Glabello-occipital length), XCB (Maximum cranial breadth), ZYB (Bizygomatic breadth), BBH (Basion-bregma height).
*   **Curated source in this repo:** `geanes/bioanth` (Ge et al., University of Tennessee Forensic Anthropology Data Bank) - `inst/extdata/howell.csv` - accessed via `raw.githubusercontent.com`. This version removes transcription errors from the original UTK files.

Full documentation: Howells, W.W. (1989) *Skull Shapes and the Map* and Howells (1995) *Who's Who in Skulls*.

### 2. Repository Structure
