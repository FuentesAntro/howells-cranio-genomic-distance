# 1. Load dependencies
install.packages(c("dplyr", "tidyr", "ggplot2", "pheatmap"))
library(dplyr); library(tidyr); library(ggplot2); library(pheatmap)

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
         filename = "figures/heatmap_morphological_distance.png")

# 6. PCA on individual-level data
pca <- prcomp(raw[, -c(1,2)], scale. = TRUE)
summary(pca)
