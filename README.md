# Howells Cranio-Genomic Distance: Population Structure from Craniofacial Morphology

[![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)](LICENSE)

**TL;DR:** Does cranial morphology preserve population history? Using 2,524 skulls from 28 worldwide populations (Howells 1973-1989), this project shows that it does. Morphological distance strongly correlates with geographic isolation, with three distinct clusters and extreme divergence (>12 Euclidean units) in long-term isolates.

| Key Metric | Detail |
| :--- | :--- |
| **Dataset** | Howells Craniometric Dataset (W.W. Howells, Harvard) |
| **Sample** | 2,524 individuals, 28 populations, 57 measurements |
| **Core Variables** | GOL (glabello-occipital length), XCB (max cranial breadth) + 55 others |
| **Methods** | Population means, standardized Euclidean distance, Ward.D2 hierarchical clustering, PCA |
| **Stack** | R (dplyr, ggplot2, pheatmap), Python (pandas), Power BI (DAX) |

---

### Figure 1 — Morphological Distance Matrix (Primary Result)

<p align="center">
  <img src="figures/heatmap_morphological_distance.png" width="100%">
</p>

**Figure 1. Pairwise morphological distance between 28 populations.**
Euclidean distance computed on standardized population means. Hierarchical clustering (Ward.D2). Scale: Blue (0) = morphologically identical, Red (13) = highly divergent.

**Interpretation:** The matrix reveals strong population structure, not random variation.

*   **Polynesian Cluster (Distance 2-4):** EASTER I, N MAORI, S MAORI, ARIKARA, MORIORI. Low internal distance, consistent with recent shared ancestry and expansion.
*   **East Asia-Pacific Cluster (Distance 3-5):** ANYANG, AINU, GUAM, MOKAPU, HAINAN, S JAPAN, N JAPAN, PHILLIPI. Tight cluster reflecting regional continuity.
*   **Isolated Outliers (Distance >12):** ANDAMAN, BUSHMAN, BURIAT, ESKIMO. Maximum divergence from all other groups. ANDAMAN vs. BURIAT reaches the highest distance (12.9), supporting long-term isolation, drift, and local adaptation as drivers of craniofacial divergence.

Data source: `distancia_morfologica.csv`

### Figure 2 — Principal Component Analysis of Individual Variation

<p align="center">
  <img src="figures/pca_howells.png" width="100%">
</p>

**Figure 2. PCA of 2,524 crania (57 measurements).**
PC1 (27.9%) captures overall cranial size and length-breadth proportion. PC2 (8.6%) captures facial vs. vault variation. Each point is an individual, colored by population.

While individual overlap is high — expected for a single species — population centroids are clearly separated. Isolates like BURIAT and ANDAMAN occupy the periphery of morphospace, confirming the pattern from Figure 1 at the individual level. This validates that population-level averaging does not create artificial clusters.

### Figure 3 — Power BI Dashboard: GOL vs XCB

<p align="center">
  <img src="figures/powerbi_GOL_XCB_promedio_poblacion.png" width="100%">
</p>

**Figure 3. Mean cranial length (GOL) vs. breadth (XCB) per population.**
X-axis: Glabello-occipital length (GOL) mm, Y-axis: Maximum cranial breadth (XCB) mm. Each point is a population mean (n=28).

**Outlier analysis:**
*   **ANDAMAN (164.5 mm GOL, 133.4 mm XCB):** Smallest skulls in the dataset. Classic island effect and long-term isolation in the Andaman Islands.
*   **BURIAT (177.3 mm GOL, 151.7 mm XCB):** Broadest skulls. Consistent with cold adaptation in Siberia (brachycephalization).

Interactive file: `howells_dashboard.pbix` — includes DAX measures `Avg_GOL` and `Avg_XCB`.

---

### Methods & Tech Stack

| Stage | Tool | Implementation |
| :--- | :--- | :--- |
| **Data Cleaning** | R | `howells_raw.csv` → filtering, outlier check, aggregation to population means |
| **Distance Matrix** | R | Scale (z-score) + Euclidean distance → `distancia_morfologica.csv` |
| **Clustering** | R | `hclust(method="ward.D2")` + `pheatmap` with dendrograms |
| **Multivariate** | R | PCA with `prcomp`, visualization with `ggplot2` |
| **Dashboarding** | Power BI | Scatter with population legend, DAX calculated tables |

### Repository Structure
