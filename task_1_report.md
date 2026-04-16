# Task 1: Git, GitHub, and EDA Report

## 1. Project Setup
- **Repository**: `Financial-analysis`
- **Branch**: `task-1`
- **Structure**: Followed standard folders: `src/`, `notebooks/`, `scripts/`, `tests/`, `.github/`.
- **CI/CD**: Initialized GitHub Actions workflow `unittests.yml` for automated testing.

## 2. Exploratory Data Analysis (EDA)
Performed analysis on `raw_analyst_ratings.csv` (approx. 1.4 million records).

### Key Findings:
- **Publication Frequency**:
  - Found significant spikes in publication during **March 2020** (COVID-19 market onset) and **June 2020**.
  - Peak daily publication reached over **900 articles** per day on peak dates.
- **Top Publishers**:
  - Most active publishers include **Paul Quintaro**, **Lisa Levin**, and **Benzinga Newsdesk**.
  - Some publisher names are email addresses; domain analysis shows these are likely internal or associated organizations.
- **Content Analysis (Keywords)**:
  - Top keywords extracted: `stocks`, `est`, `eps`, `market`, `shares`, `earnings`, `sales`.
  - This confirms the dataset focus on corporate earnings and market updates.
- **Headline Length**:
  - Mean headline length is approximately **60-80 characters**, following standard financial news formats.

## 3. Scripts and Utilities
- Developed `src/data_loader.py` for clean data access.
- Developed `src/eda_utils.py` for reusable analysis functions.
- Developed `scripts/run_eda.py` to generate the findings reported above.

## 4. GitHub Workflow
- Commits made to `task-1` branch.
- Ready for merging into `main`.
