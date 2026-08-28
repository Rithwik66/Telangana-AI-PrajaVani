# Telangana AI–PrajaVani

## Day 3 — Source Registry

### Purpose

The source registry maintains the metadata of public Telangana government documents selected for Document Corpus v1.

Keeping this information in a structured registry makes each source traceable and helps with future document ingestion and RAG processing.

### Registry

| ID | Title | Category | Date | Source / Owner |
|---|---|---|---|---|
| D01 | Rythu Bharosa | Agriculture | Not stated | Official Government of Telangana — Department of Agriculture |
| D02 | Aasara Pensions | Social Welfare | 01/10/2018 (page record) | Hyderabad District, Government of Telangana |
| D03 | Kalyana Lakshmi / Shaadi Mubarak | Welfare / Revenue | 02/10/2014 (page record) | Rajanna Sircilla District, Government of Telangana |
| D04 | Mission Bhagiratha — Citizens Charter | Water Supply | Published 2025 (search record) | Mission Bhagiratha, Government of Telangana |
| D05 | Housing for the Poor / 2BHK | Housing | 05/03/2016 (page record) | Yadadri Bhuvanagiri District, Government of Telangana |
| D06 | Roads and Buildings Department | Roads / Transport | Not stated | Telangana State Portal |
| D07 | TSROADS Grievance Form | Roads / Civic | Not stated | Roads and Buildings Department, Government of Telangana |

### Required Metadata

Each source should maintain:

- Source ID
- Title
- Category
- Date information
- Source or owner
- Source URL
- Intended use

### Date Handling

Dates should only be recorded when supported by the source material.

If a publication date is unavailable, the registry should explicitly use:

**Not stated**

This prevents unsupported dates from being introduced into the corpus.

### Source Traceability

Every document included in the corpus should remain linked to its originating government source.

This allows future retrieved information to be traced back to the original source document.

### Intended Use

The registry will support future:

- Document ingestion
- Cleaning and preprocessing
- Chunking
- Metadata tagging
- Embedding generation
- Vector retrieval
- RAG-based scheme and policy recommendations 