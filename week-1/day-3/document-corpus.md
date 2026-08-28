# Telangana AI–PrajaVani

## Day 3 — Public Document Collection

### Purpose

The Day 3 task is to build the first public-document corpus for Telangana AI–PrajaVani.

The corpus contains authoritative Telangana government scheme, policy, and civic-information sources that can later be processed and used by the project's knowledge and retrieval system.

### Day 3 Objectives

1. Collect public Telangana government scheme, policy, and civic-information sources.
2. Prioritize official state and district government sources.
3. Record the source URL, title, available date information, and category for every corpus item.
4. Cover multiple domains relevant to citizen questions and civic grievances.
5. Keep source metadata so later RAG answers can be traced to the originating document.
6. Keep public knowledge sources separate from synthetic grievance data and restricted citizen information.

### Why the Corpus Is Required

AI–PrajaVani includes a Knowledge Layer that uses government document ingestion, chunking, embeddings, and retrieval.

The corpus is required because the system should provide grounded scheme and policy recommendations rather than unsupported answers.

Government information can be distributed across scheme pages, policy documents, circulars, district websites, and other public sources. Collecting these sources into a controlled corpus makes the information easier to process, retrieve, and trace.

Each document should retain source metadata so that information returned by the future RAG system can be connected back to its original government source.

### Document Corpus v1 — Metadata Registry

| ID | Title | Category | Date | Source / Owner |
|---|---|---|---|---|
| D01 | Rythu Bharosa | Agriculture | Not stated | Official Government of Telangana — Department of Agriculture |
| D02 | Aasara Pensions | Social Welfare | 01/10/2018 (page record) | Hyderabad District, Government of Telangana |
| D03 | Kalyana Lakshmi / Shaadi Mubarak | Welfare / Revenue | 02/10/2014 (page record) | Rajanna Sircilla District, Government of Telangana |
| D04 | Mission Bhagiratha — Citizens Charter | Water Supply | Published 2025 (search record) | Mission Bhagiratha, Government of Telangana |
| D05 | Housing for the Poor / 2BHK | Housing | 05/03/2016 (page record) | Yadadri Bhuvanagiri District, Government of Telangana |
| D06 | Roads and Buildings Department | Roads / Transport | Not stated | Telangana State Portal |
| D07 | TSROADS Grievance Form | Roads / Civic | Not stated | Roads and Buildings Department, Government of Telangana |

### Metadata Rules

For every corpus item, record:

- Document or source ID
- Title
- Category
- Source or owner
- Source URL
- Date, when available
- Intended use

If a source does not state a publication date in the retrieved material, record **Not stated** rather than inferring a date.

### Corpus Coverage

The initial corpus should cover different domains relevant to citizen questions and grievances, including:

- Agriculture
- Social welfare
- Welfare and revenue
- Water supply
- Housing
- Roads and transport
- Civic services

### Future Processing

The collected documents can later go through:

1. Download or source collection
2. Parsing
3. OCR where necessary
4. Cleaning
5. Chunking
6. Metadata tagging
7. Embedding generation
8. Vector retrieval
9. RAG-based use

### Expected Outcome

Document Corpus v1 provides a controlled starting set of public Telangana government sources for the future knowledge and RAG layer of AI–PrajaVani.

The corpus should remain traceable to its original sources and should be expanded as additional authoritative documents are identified. 