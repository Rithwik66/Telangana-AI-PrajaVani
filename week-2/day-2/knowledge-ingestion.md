# Telangana AI–PrajaVani

## Week 2 — Day 2
## Knowledge Ingestion

### Objective

Prepare the public Telangana government documents collected during Week 1 for use in the project's knowledge and retrieval layer.

### Ingestion Pipeline

The document ingestion process is:

Source Documents
→ Parse
→ Clean
→ Attach Metadata
→ Chunk
→ Prepare for Indexing

### 1. Document Parsing

Extract usable text from the collected government documents and web pages.

The parser should preserve important document information such as:

- Title
- Source
- URL
- Date
- Category
- Document text

### 2. Text Cleaning

Clean the extracted text before indexing.

Cleaning should include:

- Removing unnecessary whitespace
- Removing repeated navigation or page elements
- Removing irrelevant formatting
- Preserving meaningful headings and content
- Keeping the original meaning of the source

### 3. Metadata

Each document should retain metadata so retrieved information can be traced back to its source.

Required metadata includes:

| Field | Description |
|---|---|
| document_id | Unique document identifier |
| title | Document or page title |
| category | Scheme, welfare, civic service, policy, etc. |
| source | Government department or authority |
| source_url | Original source URL |
| date | Publication date when available |

If a date is unavailable, record:

**Not stated**

### 4. Document Chunking

Long documents should be divided into smaller chunks before retrieval.

Chunks should:

- Preserve meaningful sections
- Avoid cutting important information unnecessarily
- Retain document metadata
- Have a unique chunk identifier
- Remain traceable to the original document

### Chunk Metadata

Each chunk should contain:

| Field | Purpose |
|---|---|
| chunk_id | Unique chunk identifier |
| document_id | Parent document |
| title | Source title |
| category | Document category |
| source | Source authority |
| source_url | Original source |
| text | Cleaned chunk text |

### 5. Corpus Separation

The public knowledge corpus must remain separate from:

- Synthetic grievance datasets
- Model evaluation datasets
- Restricted citizen information

Only appropriate public government information should enter the knowledge corpus.

### 6. Quality Checks

Before indexing, verify:

- [ ] Text was successfully extracted.
- [ ] Irrelevant page content was removed.
- [ ] Metadata is attached.
- [ ] Source URL is retained.
- [ ] Missing dates are marked as "Not stated".
- [ ] Chunks contain meaningful text.
- [ ] Every chunk can be traced to its source document.
- [ ] No restricted citizen information is included.

### Expected Outcome

The public Telangana government documents are parsed, cleaned, metadata-tagged, and divided into traceable chunks ready for the next stage: embeddings and retrieval.