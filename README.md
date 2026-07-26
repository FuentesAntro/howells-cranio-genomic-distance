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

howells/
├── howells.Rproj
├── R/
│ └── 01_pca.R # PCA and visualization workflow
├── data/
│ ├── raw/
│ │ └── howells_raw.csv # 2524 x 83 (with ID, Sex, Pop)
│ └── processed/
│ └── distancia_morfologica.csv # Pairwise Mahalanobis-like distance (10 PCs)
├── figures/
│ └── pca_howells.png # PC1 vs PC2 by population
└── README.md

Code

### 3. Methods

**3.1 Pre-processing**
- Removal of zero-variance columns (e.g., TBA, BSA) corresponding to absent measurements in this curated version.
- No imputation; complete-case analysis for PCA.

**3.2 Morphometric Variability**
- **Standardization:** Variables centered and scaled (z-score) to account for scale differences.
- **Principal Component Analysis (PCA):** `prcomp(..., center=TRUE, scale.=TRUE)` on all informative craniometric variables.
- **Visualization:** PC1 (~20% variance) captures overall cranial size and vault length; PC2 (~11% variance) captures facial breadth vs. neurocranial breadth.

**3.3 Morphological Distance**
- Population centroids computed on the first 10 PCs (>60% total variance).
- Pairwise Euclidean distance between centroids = morphological distance matrix (`distancia_morfologica.csv`).

**3.4 Next Step - Genomic Distance (Roadmap)**
- Compute Weir & Cockerham Fst from 1000 Genomes Phase 3 for populations proxying Howells groups.
- Mantel test: `mantel(morph_dist, genomic_dist, method="pearson", permutations=9999)`.

### 4. Results

**Figure 1: Global Cranial Variation**

![PCA Howells](figures/pca_howells.png)

- Clear but overlapping clusters. NORSE/BERG/ZALAV (European) vs. ZULU/DOGON/TEITA (Sub-Saharan African) vs. N-JAPAN/S-JAPAN/AINU/ATAYAL (East Asian/Pacific) separate along PC1/PC2.
- Continuous variation supports the model of human cranial diversity as clinal with regional patterning, consistent with Howells (1973, 1989).

Morphological distance matrix preview: Closest pairs: N-JAPAN / S-JAPAN; Farthest: BUSHMAN / NORSE.

### 5. Reproducibility

```r
# 0. Clone and download data
dir.create("data/raw", recursive=TRUE, showWarnings=FALSE)
download.file("https://raw.githubusercontent.com/geanes/bioanth/master/inst/extdata/howell.csv",
              "data/raw/howells_raw.csv", mode="wb")

# 1. PCA workflow
library(tidyverse)
df <- read.csv("data/raw/howells_raw.csv")
medidas <- df %>% select(GOL:OCA) %>% select(where(~var(., na.rm=TRUE) > 0))
pca <- prcomp(medidas, center=TRUE, scale.=TRUE)

# 2. Save figures and distances
dir.create("figures", showWarnings=FALSE)
dir.create("data/processed", recursive=TRUE, showWarnings=FALSE)

Requirements: R >= 4.2, tidyverse, ggplot2

6. Citation
Howells, W. W. (1973). Cranial Variation in Man: A Study by Multivariate Analysis of Patterns of Difference Among Recent Human Populations. Peabody Museum Papers, 67.

Howells, W. W. (1989). Skull Shapes and the Map. Papers of the Peabody Museum, vol. 79.

Fuentes, A. (2026). howells-cranio-genomic-distance. GitHub: https://github.com/FuentesAntro/howells-cranio-genomic-distance

7. License
Data: Public Domain (Howells data is in the public domain). Code: MIT License.
