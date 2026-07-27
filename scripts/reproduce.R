# Howells Cranio-Genomic Distance - Reproducible pipeline
# Author: FuentesAntro

# 1. Load dependencies
# install.packages(c("dplyr", "tidyr", "ggplot2", "pheatmap")) # Run only once
library(dplyr)
library(tidyr)
library(ggplot2)
library(pheatmap)

# 2. Load raw data
raw <- read.csv("data/raw/howells_raw.csv")

# 3. Aggregate to population means and standardize
pop_means <- raw %>%
  group_by(Population) %>%
  summarise(across(where(is.numeric), mean, na.rm = TRUE))

pop_scaled <- scale(pop_means[, -1])
rownames(pop_scaled) <- pop_means$Population

# 4. Compute Euclidean distance matrix
dist_matrix <- dist(pop_scaled, method = "euclidean")
write.csv(as.matrix(dist_matrix), "data/processed/distancia_morfologica.csv")

# 5. Hierarchical clustering (Ward.D2) and heatmap
pheatmap(as.matrix(dist_matrix),
         clustering_method = "ward.D2",
         filename = "figures/heatmap_morphological_distance.png",
         width = 10, height = 10)

# 6. PCA on individual-level data
# Excludes first 2 columns (ID and Population)
pca_data <- raw %>% select(where(is.numeric))
pca <- prcomp(pca_data, scale. = TRUE)
summary(pca)

# Optional: Save PCA plot
# ggsave("figures/pca_howells.png")
