# Howells Cranio-Genomic Distance

Craniofacial variation in 28 populations (n=2524) — Howells dataset (1973-1989). Analysis of morphological divergence and geographic isolation.

**Dataset:** W.W. Howells, Harvard | **Tools:** R, Python, Power BI | **License:** MIT

---

## Main Results

### Figure 1 — Morphological Distance Matrix

<img src="figures/heatmap_morphological_distance.png" width="100%">

**Figure 1. Morphological distance between 28 populations (n=2524).**
Euclidean distance with hierarchical clustering. Blue = low distance (morphologically close), Red = high distance (divergent).

Three structure levels:
1.  **Polynesian cluster** — EASTER I, N/S MAORI, ARIKARA, MORIORI
2.  **East Asia-Pacific cluster** — ANYANG, AINU, GUAM, MOKAPU, HAINAN, N/S JAPAN, PHILIPPI
3.  **Highly divergent isolates** — ANDAMAN, BUSHMAN, BURIAT, ESKIMO (distances >12)

Consistent with long-term geographic isolation and genetic drift.

### Figure 2 — Power BI: GOL vs XCB

<img src="figures/powerbi_GOL_XCB_promedio_poblacion.png" width="100%">

**Figure 2. Average cranial dimensions per population.**
X = Glabello-occipital length (GOL) mm, Y = Maximum cranial breadth (XCB) mm. Average per population (28 points).

ANDAMAN shows the smallest values (164 mm), reflecting island isolation. BURIAT shows the highest breadth (151 mm).

> Interactive dashboard: `howells_dashboard.pbix`

---

## Repository

| Folder / File | Content |
| :--- | :--- |
| `data/` | Raw Howells craniometric data |
| `figures/` | High-resolution plots |
| `howells_dashboard.pbix` | Power BI interactive file |
| `LICENSE` | MIT |

## Methods

1.  Population means calculated for GOL, XCB and 20 additional measurements (R).
2.  Euclidean distance matrix computed on standardized means.
3.  Hierarchical clustering (Ward.D2) and heatmap visualization.
4.  Interactive scatter plot in Power BI with DAX measures `Avg_GOL` and `Avg_XCB`.

## Conclusion

Cranial morphology clusters by geography. Isolated populations show the greatest divergence, supporting isolation-by-distance model in human craniofacial variation.

---
**Author:** FuentesAntro — Biological Anthropology 2025/26
