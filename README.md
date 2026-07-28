# Craniometric Biodistance Analysis: Testing Geographic Isolation in Global Skull Morphology

Multivariate morphometric analysis testing whether cranial shape variation across 28 worldwide populations reflects geographic isolation and population history, using standard biodistance methodology from biological anthropology.

<p align="left">
<img src="https://img.shields.io/badge/R-4.x-276DC3?style=flat-square&logo=r&logoColor=white" alt="R">
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black" alt="Power BI">
<img src="https://img.shields.io/badge/License-MIT-4CAF50?style=flat-square" alt="MIT License">
</p>

---

## Context and Scientific Framing

This project applies **biodistance analysis** — a well-established, peer-reviewed method in biological anthropology and bioarchaeology used to reconstruct population relationships from skeletal morphology (Howells 1973, 1989; Relethford 2004). It is a multivariate statistics exercise, not an ancestry-estimation or forensic tool.

Two points of consensus in the literature frame this analysis and are worth stating explicitly:

1. **Cranial variation is clinal, not typological.** Numerous studies using this exact dataset (Relethford 2004; Roseman 2004; Harvati & Weaver 2006; von Cramon-Taubadel 2009) show that global craniometric variation correlates with *neutral genetic distance* under an isolation-by-distance model — the same process that shapes allele frequencies. It does **not** support discrete racial categories; Relethford (2009) addresses this directly.
2. **Morphology is a proxy, not genomic data.** Cranial shape is a phenotypic signal shaped by population history (genetic drift, gene flow) and, to a lesser extent, climate and mechanical adaptation. It correlates with — but does not measure — genomic ancestry.

The goal of this project is methodological: to demonstrate a full multivariate statistics pipeline (distance matrices, hierarchical clustering, PCA, BI dashboarding) applied to a classic open dataset in the discipline, not to draw conclusions about individuals or present-day groups.

---

## TL;DR

Does skull shape carry a signature of geographic isolation? Using the Howells craniometric dataset (2,524 individuals, 28 populations, 57 measurements), this project computes population-level morphological distances and tests them against clustering and dimensionality-reduction methods. Consistent with the isolation-by-distance literature above, historically isolated populations — Andaman Islanders, San (Bushman), Buriat, and Arctic Eskimo — separate from the global sample at distances exceeding 12 standard units, matching the pattern expected from genetic drift and founder effects acting on small, isolated founding populations.

---

## Key Metrics

| Metric | Value |
|---|---|
| Populations | 28, worldwide distribution |
| Sample size (n) | 2,524 individual crania |
| Craniometric variables | 57 standard measurements (Howells protocol) |
| Aggregation level | Population means, z-standardized |
| Distance metric | Euclidean distance on standardized means |
| Clustering method | Hierarchical, Ward's minimum variance (Ward.D2) |
| Dimensionality reduction | PCA — PC1 = 27.9% variance, PC2 = 8.6% variance |
| Time depth of source data | Data collected 1965–1980 (Howells, published 1973–1989) |

---

## Main Results

### Figure 1 — Morphological Distance Matrix and Hierarchical Clustering

<p align="center">
<img src="figures/heatmap_morphological_distance.png.png" width="100%">
</p>

**Method.** Population means for all 57 craniometric variables were z-standardized to remove scale effects across measurements with different units and ranges. A pairwise Euclidean distance matrix was computed across the 28 populations and submitted to hierarchical agglomerative clustering using Ward's minimum variance criterion (Ward.D2). The resulting matrix is rendered as a heatmap with dendrograms on both axes; color encodes morphological distance from blue (low, 0) to red (high, 13).

**Findings.** The clustering resolves three principal groupings:

1. **Polynesia / Remote Oceania** — EASTER I, N/S MAORI, ARIKARA, MORIORI form a tight cluster, consistent with shared Austronesian-derived ancestry and serial founder effects across the Pacific.
2. **East Asia–Pacific Rim** — ANYANG, AINU, GUAM, MOKAPU, HAINAN, N/S JAPAN, and PHILIPPINES group together, reflecting geographic contiguity and gene flow across continental and near-shore East Asia.
3. **Isolated outliers (distance > 12)** — ANDAMAN, BUSHMAN, BURIAT, and ESKIMO each split off early in the dendrogram. These four populations share a common demographic profile: small effective population size and long-term geographic or reproductive isolation — the expected statistical signature of drift acting on small founding groups, as documented in the isolation-by-distance literature cited above.

The pattern supports an isolation-by-distance model: morphological divergence scales with historical geographic and reproductive isolation, not with any discrete typology.

---

### Figure 2 — Principal Component Analysis of Cranial Shape Variation

<p align="center">
<img src="figures/pca_howells.png" width="100%">
</p>

**Method.** PCA was applied to all 57 measurements at the individual level (n = 2,524), preserving within-population variance rather than collapsing to means. Each point represents one cranium, colored by population of origin (28 categories).

**Findings.** PC1 accounts for 27.9% of total variance and PC2 for 8.6% (36.5% combined) — a substantial share for a 57-dimensional dataset, indicating that a small number of underlying shape axes (general cranial size and an elongation/breadth axis) structure most of the variation. Population clusters show **extensive overlap** along both axes — the expected result for a continuously varying, clinally distributed trait: cranial morphology does not partition into discrete, non-overlapping types. At the same time, population centroids are visibly displaced from one another, and the same outlier populations from Figure 1 occupy the periphery of the PC1–PC2 space. This dual pattern — global overlap with detectable structure — is the textbook signature of human biological variation described in the literature: clinal, not categorical.

---

### Figure 3 — Interactive Dashboard: Cranial Length vs. Breadth by Population

<p align="center">
<img src="figures/powerbi_GOL_XCB_promedio_poblacion.png.png" width="100%">
</p>

**Method.** A Power BI dashboard was built on the aggregated dataset, with DAX measures `Avg_GOL` (Glabello-Occipital Length) and `Avg_XCB` (Maximum Cranial Breadth) computed per population.

**Findings.** Two populations depart from the main distribution:

- **ANDAMAN** — lowest average GOL (164.5 mm), consistent with an insular effect: small, long-isolated island populations with reduced body and cranial size, plausibly linked to constrained resource availability and founder effects.
- **BURIAT** — highest average XCB (151 mm), producing a markedly brachycephalic (broad) cranial vault, consistent with cold-climate adaptation described in the literature (a pattern paralleling Bergmann's and Allen's ecogeographic rules).

These two extremes reinforce the same conclusion drawn from the distance matrix and PCA: cranial shape tracks the ecological and demographic history of each population, not a single global cline.

---

## Methods and Tech Stack

| Layer | Tools | Purpose |
|---|---|---|
| Data cleaning and wrangling | R (`dplyr`, `tidyr`) | Raw data validation, missing-value handling, population-level aggregation |
| Statistical analysis | R (base `stats`, `dist()`, `hclust()`) | Euclidean distance matrix, Ward.D2 hierarchical clustering, PCA |
| Visualization (static) | R (`ggplot2`, `pheatmap`) | Heatmap with dendrograms, PCA scatter plot |
| Exploratory analysis | Python (`pandas`, `seaborn`) | Cross-validation of aggregation logic and exploratory plotting |
| Business intelligence | Power BI (DAX: `Avg_GOL`, `Avg_XCB`) | Interactive population-level dashboard |
| Version control | Git / GitHub | Reproducibility and project history |

---

## Repository Structure

```
craniometric-biodistance-howells/
├── data/
│   ├── raw/
│   │   └── howells_raw.csv
│   └── processed/
│       └── morphological_distance_matrix.csv
├── figures/
│   ├── heatmap_morphological_distance.png.png
│   ├── pca_howells.png
│   └── powerbi_GOL_XCB_promedio_poblacion.png.png
├── scripts/
│   ├── reproduce.R
│   └── exploratory_check.py
├── dashboard/
│   └── howells_dashboard.pbix
├── .gitignore
├── LICENSE
└── README.md
```

### Power BI dashboard

1. Open `howells_dashboard.pbix` in Power BI Desktop.
2. Update the data source connection to point to `data/processed/morphological_distance_matrix.csv` and `data/raw/howells_raw.csv`.
3. Refresh the model (`Home → Refresh`) to recompute the `Avg_GOL` and `Avg_XCB` DAX measures.
4. Interact with the scatter plot to filter by population or region.

---

## Scope and Limitations

- **Proxy, not genomic data.** Cranial measurements are a phenotypic proxy correlated with neutral genetic distance at the population level (Relethford 2004); they are not a substitute for genomic ancestry data and are not used here to infer individual ancestry.
- **Historical dataset.** Data were collected 1965–1980 on museum and reference collections; population labels reflect the sampling and terminology of that period, not present-day self-identification.
- **Population-level, not individual-level, claims.** All findings describe statistical patterns across population means. No claims are made — or supportable — about any individual.
- **Purpose.** This repository exists to demonstrate a multivariate statistics and BI pipeline (distance matrices, hierarchical clustering, PCA, dashboarding) on a canonical open dataset in biological anthropology, not to advance new claims in population history research.

---

## Conclusion

Cranial morphology in the Howells dataset is not randomly distributed across geography: it clusters populations by continental and insular proximity, and it isolates precisely the populations with the strongest independent demographic histories — the Andaman Islanders, San, Buriat, and Eskimo — as the most morphologically distant from the global sample. This is the expected outcome under an isolation-by-distance model of human biological variation, in line with the broader biological anthropology literature (Relethford 2004, 2009), where drift and localized adaptation accumulate in proportion to a population's reproductive isolation rather than under any model of discrete, bounded types. The convergent evidence from hierarchical clustering, PCA, and dashboard analysis across three independent analytical approaches strengthens confidence in this conclusion beyond what any single method would support alone.

---

## Citations

Howells, W. W. (1973). *Cranial Variation in Man.* Papers of the Peabody Museum, Harvard University.
Howells, W. W. (1989). *Skull Shapes and the Map.* Papers of the Peabody Museum, Harvard University.
Relethford, J. H. (2004). Global patterns of isolation by distance based on genetic and morphological data. *Human Biology*, 76(4), 499–513.
Relethford, J. H. (2009). Race and global patterns of phenotypic variation. *American Journal of Physical Anthropology*, 139(1), 16–22.

---

**Author:** Antonio Fuentes Moreno — Social and Cultural Anthropology, Universidad de Sevilla, 2025/26
**License:** MIT
