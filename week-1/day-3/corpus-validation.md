# Telangana AI–PrajaVani

## Day 3 — Corpus Validation

### Validation Checklist

- [ ] Public Telangana government sources have been identified.
- [ ] Official state or district government sources are prioritized.
- [ ] Source title is recorded for each corpus item.
- [ ] Source category is recorded.
- [ ] Available date information is recorded.
- [ ] Source or owner is recorded.
- [ ] Source URL is retained for traceability.
- [ ] Public knowledge sources are kept separate from synthetic grievance data.
- [ ] Restricted citizen information is not included in the public corpus.
- [ ] Corpus metadata is ready for future ingestion and RAG processing.

### Corpus Quality Principles

#### Authority

Prefer official Telangana government and district government sources.

#### Traceability

Every source should be traceable to its originating page or document.

#### Accuracy

Do not infer missing publication dates or unsupported metadata.

#### Relevance

Sources should relate to government schemes, policies, civic services, or information useful for citizen grievances.

#### Separation

The public document corpus should remain separate from synthetic grievance datasets and restricted citizen information.

### Future RAG Preparation

The validated corpus can later be processed through:

**Source Collection → Parsing → Cleaning → Chunking → Metadata Tagging → Embeddings → Vector Retrieval → RAG**

### Expected Outcome

The Day 3 corpus validation establishes a controlled and traceable set of public Telangana government sources that can be prepared for the project's future knowledge and retrieval layer. 