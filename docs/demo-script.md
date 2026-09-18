# Portfolio Demo Script

## 1. Introduce the Problem

Small businesses often store operational knowledge in documents that are difficult to search quickly.

## 2. Show Authentication

Register and log in through Swagger.

Explain that documents and conversations are isolated by user.

## 3. Upload Business Knowledge

Upload:

```text
demo_data/automation_services.txt
```

Index the document.

## 4. Show Semantic Retrieval

Ask a paraphrased question:

```text
Can this business automate lead follow-up and repetitive tasks?
```

Show that retrieval finds the relevant document even when the wording differs.

## 5. Show Grounded Answer Generation

Use:

```text
POST /api/chat/ask
```

Explain that Jina handles embeddings, pgvector handles retrieval, and Groq generates the answer from retrieved context.

## 6. Show Hallucination Resistance

Ask:

```text
What is the weather in Berlin today?
```

Show:

```text
grounded: false
```

and the safe insufficient-information response.

## 7. Show Operations

Open:

```text
/health
/ready
/release
/api/admin/metrics
```

Explain request IDs, structured logs, retries, and metrics.

## 8. Show Security

Mention:

- JWT authentication
- Argon2 password hashing
- user ownership isolation
- admin authorization
- rate limiting
- upload validation
- security headers
- non-root Docker execution

## 9. Close

The project demonstrates an end-to-end AI system rather than a single LLM API call.
