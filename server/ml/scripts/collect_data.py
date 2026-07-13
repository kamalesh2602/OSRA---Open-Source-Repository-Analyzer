from pathlib import Path
import requests
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm
import os

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "repositories.csv"
OUTPUT_FILE = BASE_DIR / "data" / "raw" / "repository_dataset.csv"


# -----------------------------
# GitHub API Functions
# -----------------------------
def get_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Failed: {owner}/{repo}")
        return None

    return response.json()


def extract_metadata(repo_data):
    return {
        "owner": repo_data["owner"]["login"],
        "repository": repo_data["name"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "watchers": repo_data["watchers_count"],
        "open_issues": repo_data["open_issues_count"],
        "size": repo_data["size"],
        "language": repo_data["language"],
        "default_branch": repo_data["default_branch"],
        "has_wiki": repo_data["has_wiki"],
        "has_projects": repo_data["has_projects"],
        "has_issues": repo_data["has_issues"],
        "has_pages": repo_data["has_pages"],
        "archived": repo_data["archived"],
        "disabled": repo_data["disabled"],
        "created_at": repo_data["created_at"],
        "updated_at": repo_data["updated_at"],
        "pushed_at": repo_data["pushed_at"],
    }


# -----------------------------
# Main Function
# -----------------------------
def collect_data():
    repositories = pd.read_csv(INPUT_FILE)

    dataset = []

    for _, row in tqdm(repositories.iterrows(), total=len(repositories)):
        repo = get_repository(row["owner"], row["repo"])

        if repo:
            dataset.append(extract_metadata(repo))

    df = pd.DataFrame(dataset)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nDataset saved to:\n{OUTPUT_FILE}")
    print(f"Repositories collected: {len(df)}")


if __name__ == "__main__":
    collect_data()