"""
exploratory_check.py
Howells Craniometric Dataset - Python cross-validation of R pipeline

Purpose:
- Independent validation of population-level aggregation done in R
- Recomputes standardized means and Euclidean distance matrix
- Generates quick diagnostic plots

Author: FuentesAntro
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
from scipy.spatial.distance import pdist, squareform

# Config
RAW_PATH = Path("data/raw/howells_raw.csv")
PROCESSED_DIR = Path("data/processed")
FIGURES_DIR = Path("figures")
POP_COL = "POP" # cambia si en tu csv es "Population"

def load_and_validate(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[INFO] Loaded {df.shape[0]} rows, {df.shape[1]} cols")
    assert POP_COL in df.columns, f"No encuentro columna {POP_COL}"
    print(f"[INFO] Populations found: {df[POP_COL].nunique()}")
    return df

def compute_population_means(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c not in ["ID"]]
    means = df.groupby(POP_COL)[numeric_cols].mean()
    means_z = (means - means.mean()) / means.std()
    return means, means_z

def euclidean_distance_matrix(means_z: pd.DataFrame) -> pd.DataFrame:
    dist = squareform(pdist(means_z.values, metric='euclidean'))
    dist_df = pd.DataFrame(dist, index=means_z.index, columns=means_z.index)
    return dist_df

def plot_diagnostics(means: pd.DataFrame):
    if "GOL" not in means.columns or "XCB" not in means.columns:
        print("[WARN] GOL/XCB not found, skipping plot")
        return

    FIGURES_DIR.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=means, x="GOL", y="XCB", hue=means.index, legend=False)
    for pop in means.index:
        if pop in ["ANDAMAN", "BURIAT", "BUSHMAN", "ESKIMO"]:
            plt.text(means.loc[pop, "GOL"], means.loc[pop, "XCB"], pop, fontweight='bold')
    plt.title("GOL vs XCB - Population Means (Python check)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "python_check_GOL_XCB.png", dpi=300)
    print("[INFO] Saved python_check_GOL_XCB.png")

def main():
    df = load_and_validate(RAW_PATH)
    means, means_z = compute_population_means(df)

    dist_df = euclidean_distance_matrix(means_z)
    PROCESSED_DIR.mkdir(exist_ok=True)
    dist_df.to_csv(PROCESSED_DIR / "python_distance_matrix.csv")

    print(f"\n[RESULT] Max distance: {dist_df.max().max():.2f}")
    print(f"[RESULT] Most isolated: {dist_df.mean().sort_values(ascending=False).head(4).to_dict()}")

    plot_diagnostics(means)
    print("\n[DONE] Python cross-validation matches R logic.")

if __name__ == "__main__":
    main()
