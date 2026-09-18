# Architecture

## Version 0.2.0 Scope

Version 0.2.0 adds document ingestion to the project foundation.

## High-Level Architecture

```text
Client
  |
  v
FastAPI
  |
  +--> Health API
  |
  +--> Documents API
          |
          v
     Document Service
          |
          +--> Validation
          +--> Local File Storage
          +--> Text Extraction
          |
          v
     Repository Layer
          |
          v
      PostgreSQL
```

## Document Ingestion Flow

```text
Upload
  |
  v
Validate extension
  |
  v
Validate file size
  |
  v
SHA-256 duplicate check
  |
  v
Store file
  |
  v
Extract text
  |
  v
Store document metadata + extracted text
```

## Supported Formats

- PDF
- TXT
- Markdown

## Security Notes

- executable files are rejected by extension allowlist
- upload size is limited
- stored filenames are generated server-side
- original user filenames are never used as storage paths
- uploaded files are excluded from Git
- SHA-256 is used for duplicate detection

## Next Architecture Step

Version 0.3.0 will introduce:

- document chunking
- embeddings
- pgvector columns
- vector similarity retrieval
- retrieval tests
