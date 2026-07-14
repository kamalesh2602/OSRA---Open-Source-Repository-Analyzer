from pathlib import Path
import json

import pandas as pd

# ---------------------------------------------------
# Paths
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATASET = BASE_DIR / "data" / "processed" / "processed_dataset.csv"
CLUSTER_DATASET = BASE_DIR / "data" / "processed" / "clustered_dataset.csv"

ARTIFACTS = BASE_DIR / "artifacts"

SUMMARY_FILE = ARTIFACTS / "cluster_summary.csv"
JSON_FILE = ARTIFACTS / "cluster_metadata.json"

# ---------------------------------------------------
# Load datasets
# ---------------------------------------------------
raw_df = pd.read_csv(RAW_DATASET)
cluster_df = pd.read_csv(CLUSTER_DATASET)

raw_df["cluster"] = cluster_df["cluster"]

# ---------------------------------------------------
# Numeric Summary
# ---------------------------------------------------
numeric_columns = [
    "stars",
    "forks",
    "watchers",
    "subscribers",
    "contributors",
    "releases",
    "branches",
    "open_issues",
    "size",
    "readme_size",
]

summary = (
    raw_df.groupby("cluster")[numeric_columns]
    .mean()
    .round(2)
)

summary["repositories"] = raw_df.groupby("cluster").size()

# ---------------------------------------------------
# Cluster Naming
# ---------------------------------------------------
metadata = {}

summary["name"] = ""
summary["insight"] = ""

for cluster in summary.index:

    stars = summary.loc[cluster, "stars"]
    contributors = summary.loc[cluster, "contributors"]
    releases = summary.loc[cluster, "releases"]
    size = summary.loc[cluster, "size"]
    repositories = int(summary.loc[cluster, "repositories"])

    # -----------------------------------------------
    # Cluster Name
    # -----------------------------------------------
    if stars >= 200000:
        name = "Enterprise Scale Projects"

        insight = (
            "These repositories represent globally adopted open-source "
            "projects with massive communities, extensive ecosystem support, "
            "and widespread production usage."
        )

    elif stars >= 100000 and releases >= 15:
        name = "Highly Active Ecosystem"

        insight = (
            "These repositories combine high popularity with frequent "
            "releases and active maintenance, indicating a healthy and "
            "continuously evolving project."
        )

    elif stars >= 10000:
        name = "Established Open Source"

        insight = (
            "These repositories have established communities, consistent "
            "development activity, and are commonly used in real-world "
            "applications."
        )

    elif stars >= 500:
        name = "Growing Community Projects"

        insight = (
            "These repositories are actively growing with moderate community "
            "adoption and regular development."
        )

    else:
        name = "Small & Experimental Projects"

        insight = (
            "These repositories are typically personal projects, prototypes, "
            "or newly created repositories with limited community activity."
        )

    summary.loc[cluster, "name"] = name
    summary.loc[cluster, "insight"] = insight

    metadata[int(cluster)] = {
        "cluster": int(cluster),
        "name": name,
        "insight": insight,
        "repositories": repositories,
        "average_stars": float(stars),
        "average_forks": float(summary.loc[cluster, "forks"]),
        "average_watchers": float(summary.loc[cluster, "watchers"]),
        "average_contributors": float(contributors),
        "average_releases": float(releases),
        "average_size": float(size),
    }

# ---------------------------------------------------
# Save
# ---------------------------------------------------
ARTIFACTS.mkdir(
    parents=True,
    exist_ok=True,
)

summary.to_csv(
    SUMMARY_FILE,
)

with open(
    JSON_FILE,
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        metadata,
        f,
        indent=4,
    )

print("\nCluster Analysis Completed")
print("=" * 60)

print(
    summary[
        [
            "name",
            "repositories",
            "stars",
            "contributors",
            "releases",
        ]
    ]
)

print(f"\nCSV  : {SUMMARY_FILE}")
print(f"JSON : {JSON_FILE}")