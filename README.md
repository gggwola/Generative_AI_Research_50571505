# Generative_AI_Research_SID

Research repository for the project **"Using Generative AI Tools – Boon or Bane"**
(REIT6811 Applied Class 6 – Comprehensive Data Handling in Research).

> Replace `SID` in the repository name with your 8-digit student ID, and update
> the Contact section below before your first push.

---

## 1. Purpose

This repository stores, organises and version-controls all materials produced by
the research team: literature, survey and interview data, analysis scripts,
drafts, reports and supporting media. It is structured so that a new collaborator
can find any file without having to ask where it lives.

---

## 2. Repository structure

```
Generative_AI_Research_SID/
├── README.md                          <- you are here
├── .gitignore                         <- files Git must never track
│
├── 01_Literature_Review/
│   ├── Journal_Articles/              <- peer-reviewed journal PDFs
│   ├── Conference_Papers/             <- conference proceedings
│   ├── Books_and_Chapters/            <- books, edited chapters
│   ├── News_and_Grey_Literature/      <- newspaper articles, reports, blogs
│   └── Reference_Library/             <- EndNote/Zotero exports (.bib, .ris)
│
├── 02_Quantitative_Analysis/
│   ├── Survey_Instrument/             <- survey questions, Qualtrics export
│   ├── Data_Raw_RESTRICTED/           <- raw survey exports (NOT committed)
│   ├── Data_Processed/                <- cleaned, de-identified datasets
│   ├── Scripts/                       <- Python / R analysis scripts
│   ├── Outputs/
│   │   ├── Figures/                   <- charts produced by the scripts
│   │   └── Tables/                    <- exported result tables
│   └── Reports/                       <- survey analysis report
│
├── 03_Qualitative_Analysis/
│   ├── Interview_Protocols/           <- interview guides, question sets
│   ├── Transcripts_Raw_RESTRICTED/    <- identifiable transcripts (NOT committed)
│   ├── Transcripts_Deidentified/      <- transcripts with identifiers removed
│   ├── Consent_Forms_RESTRICTED/      <- signed consent forms (NOT committed)
│   ├── Coding_and_Themes/             <- codebook, NVivo exports, theme matrices
│   ├── Visualisations/                <- thematic maps, word clouds
│   └── Reports/                       <- insights / findings report
│
├── 04_Drafts_and_Reports/
│   ├── Research_Proposal/
│   ├── Conference_Papers/
│   ├── Final_Report/
│   └── Presentations/
│
├── 05_Additional_Materials/
│   ├── Participant_Information_Sheets/
│   ├── Photos_and_Media/
│   └── Ethics_and_Admin/              <- ethics approval, meeting minutes
│
└── 99_Archive/                        <- superseded material kept for provenance
```

Empty folders contain a `.gitkeep` placeholder so that Git preserves the
structure. Delete it once real files are added.

---

## 3. File naming convention

All files follow:

```
YYYYMMDD_Project_Description_vNN.ext
```

Examples:

- `20260301_GenAI_SurveyData_Cleaned_v02.csv`
- `20260305_GenAI_DescriptiveStats_v01.py`
- `20260312_GenAI_InterviewTranscript_P07_Deidentified_v01.docx`
- `20260401_GenAI_FinalReport_v03.docx`

Rules:

1. **Dates as `YYYYMMDD`** so files sort chronologically.
2. **No spaces** — use underscores; reserve hyphens for within-element separation.
3. **No special characters** (`/ \ : * ? " < > | & $`) and no accents.
4. **Two-digit version numbers** (`v01`, `v02`) — never `final`, `final_final`.
5. **Keep names under ~50 characters** and avoid abbreviations the team has not agreed on.
6. **Participants are referred to by code** (`P01`, `P02`), never by name.

Rationale and further guidance:
<https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions>

---

## 4. Access control and sensitive data

Folders suffixed `_RESTRICTED` hold identifiable or sensitive material
(raw survey exports, signed consent forms, identifiable interview transcripts).
These are **excluded by `.gitignore` and must never be committed to GitHub**,
even in a private repository.

Sensitive material is stored instead in **UQ Research Data Manager (UQ RDM)**,
with access limited to named members of the research team under the project's
ethics approval. Only de-identified derivatives are version-controlled here.

Everything else in this repository is shareable within the research team.

---

## 5. How to contribute

1. **Clone** the repository (or **fork** it if you are not a direct collaborator):
   ```
   git clone https://github.com/<username>/Generative_AI_Research_SID.git
   ```
2. **Create a branch** with an informative name:
   ```
   git checkout -b feature/add-survey-cleaning-script
   ```
   Use `feature/`, `fix/`, `docs/` or `data/` prefixes.
3. **Make your changes**, then commit with a meaningful message:
   ```
   git add .
   git commit -m "Add cleaned survey data and initial descriptive analysis script"
   ```
   Write messages in the imperative mood, describing *what* changed and *why*.
   Avoid "update", "changes", "asdf".
4. **Push** and open a **pull request** against `main`.
5. A reviewer checks the changes, resolves any merge conflicts, and merges.
6. After merging, everyone should **fetch origin** and **pull origin** so their
   local `main` is up to date.

Please do not commit directly to `main`.

---

## 6. Issues

Use the **Issues** tab to record tasks, questions and problems. Label them
(`bug`, `enhancement`, `data`, `writing`) and assign an owner. Close an issue
only when the corresponding change has been merged.

---

## 7. Contact

| Role | Name | GitHub |
|---|---|---|
| Repository owner | @gggwola | `@gggwola` |
| Code reviewer | | |
| Developer | | |
| Developer | | |

---

*Last updated: 2026-09-17*
