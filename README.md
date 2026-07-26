# Craniometric Variability in 28 Global Populations (Howells Dataset)

*Biological anthropology meets applied data science — R, Python, and Power BI on 2,524 human crania*

---

**Stack:** R (tidyverse, Morpho, vegan, factoextra) · Python (pandas, scikit-learn, UMAP, Plotly) · Power BI
**Sample:** 2,524 crania · 28 populations · 57 craniometric measures
**Background:** BA in Social Anthropology (Universidad de Sevilla) → MSc in Applied Data Science (USAL–UGR)

---

## Why this project

I trained as a social anthropologist before moving into data science, and most of my early portfolio work sat on the "social" side of the field — surveys, wellbeing indicators, spatial analysis of neighborhoods. This project is the other half: **biological anthropology**, treated with the same statistical rigor and reproducible pipeline I'd apply to any social dataset.

The Howells craniometric dataset is one of the most widely used resources in physical anthropology — compiled by W.W. Howells across decades of fieldwork, it remains a standard reference for studying human cranial variation at a global scale. I wanted to know whether classic population-genetics questions (does distance predict divergence?) hold up when you swap DNA for skull shape.

## The question

**Does cranial morphological distance between populations track geographic distance?**

This is a cranial-metrics test of *isolation by distance* — the idea that populations which have been geographically separated longer tend to diverge more, in phenotype as much as in genotype. It's the same logic behind classic work by Relethford (2004) on global craniometric variation, applied here end-to-end with a full open-source pipeline.

## What's actually in the data

57 of the original 82 Howells measurements are populated across the full sample (the rest are partial/legacy fields present only in specific sub-collections), covering the core cranial vault, face, and base dimensions — glabella-occipital length, cranial breadth, basion-nasion length, and so on.

## Pipeline

| Stage | Tool | What it does |
|---|---|---|
| Cleaning & standardization | R · tidyverse | Median imputation, z-scoring by sex, population/continent crosswalk |
| Classical morphometrics | R · Morpho, factoextra | PCA on 57 standardized measures |
| Population differentiation | R · stats | MANOVA across 28 populations |
| Distance structure | R · Morpho, vegan | Mahalanobis distance between population centroids; Mantel test vs. geographic distance |
| Unsupervised structure | Python · scikit-learn, UMAP | UMAP embedding + KMeans clustering, checked against continental labels |
| Executive dashboard | Power BI | Interactive population-level comparison and KPIs |

## Results so far

**Principal component analysis**
PC1 and PC2 together separate the 28 populations along recognizable geographic lines — Sub-Saharan African and circumpolar groups sit at the vault-shape extremes, with East Asian and European populations clustering more centrally.

- **PC1 explains 27.9%** of total shape variance
- **PC2 explains 8.6%**

![PCA of cranial variability](figures/pca_pc1_pc2_continente.png)

**Population distance structure**
Pairwise Mahalanobis distances between the 28 population centroids show clear geographic blocks: Andaman Islanders, Bushman, and the two Maori samples form one distant cluster from the rest; Zalavar, Berg, and Atayal cluster together; Buriat and Eskimo pair off from the circumpolar/Northeast Asian branch. The hierarchical clustering on top of the heatmap essentially re-derives continental groupings from cranial shape alone, with a few interesting exceptions worth digging into (Polynesian samples clustering closer to Sub-Saharan African ones, for instance — a known quirk in craniometric literature, not a data error).

![Morphological distance heatmap](figures/mahalanobis_heatmap.png)

**Isolation by distance (Mantel test)**
*Formal Mantel test (morphology vs. geographic distance, 999 permutations) — result pending. Once run, the correlation coefficient and significance value go here.*

**Dashboard view**
A population-level look at two of the most discriminating measures — cranial length (GOL) and breadth (XCB) — already separates dolichocranic (long, narrow) from brachycranic (short, broad) populations at a glance.

![Power BI — GOL vs XCB by population](figures/powerbi_gol_xcb.png)

## Ethical note

This dataset draws on historical osteological collections assembled over the 19th and 20th centuries, in many cases without the consent of the communities of origin. All analysis here is statistical and aggregate — no individual-level identifiers are used, and no claims are made about the collections' provenance beyond what's documented by Howells and subsequent researchers. This kind of colonial-era collecting history is exactly what frameworks like NAGPRA exist to address, and it's worth naming explicitly rather than treating cranial data as ethically neutral just because it's decades old and freely downloadable.

## Repository structure
