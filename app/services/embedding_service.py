from typing import Literal

import httpx

from app.core.config import settings

EmbeddingTask = Literal["retrieval.passage", "retrieval.query"]


class EmbeddingProviderError(RuntimeError):
    pass


def _validate_provider() -> None:
    if settings.embedding_provider.lower() != "jina":
        raise EmbeddingProviderError(
            f"Unsupported embedding provider: {settings.embedding_provider}"
        )

    if not settings.jina_api_key:
        raise EmbeddingProviderError(
            "JINA_API_KEY is not configured. Add it to .env before indexing or retrieval."
        )


def _request_embeddings(
    texts: list[str],
    task: EmbeddingTask,
) -> list[list[float]]:
    if not texts:
        return []

    _validate_provider()

    url = f"{settings.jina_base_url.rstrip('/')}/embeddings"
    payload = {
        "model": settings.embedding_model,
        "task": task,
        "dimensions": settings.embedding_dimensions,
        "normalized": True,
        "embedding_type": "float",
        "input": texts,
    }
    headers = {
        "Authorization": f"Bearer {settings.jina_api_key}",
        "Content-Type": "application/json",
    }

    try:
        with httpx.Client(timeout=settings.embedding_timeout_seconds) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        body = exc.response.text[:1000]
        raise EmbeddingProviderError(
            f"Jina API returned HTTP {exc.response.status_code}: {body}"
        ) from exc
    except httpx.HTTPError as exc:
        raise EmbeddingProviderError(
            f"Could not connect to Jina Embeddings API: {exc}"
        ) from exc

    data = response.json().get("data")

    if not isinstance(data, list) or not data:
        raise EmbeddingProviderError("Jina API returned no embedding data.")

    ordered = sorted(data, key=lambda item: item.get("index", 0))
    embeddings = [item.get("embedding") for item in ordered]

    if any(not isinstance(embedding, list) for embedding in embeddings):
        raise EmbeddingProviderError("Jina API returned an invalid embedding payload.")

    for embedding in embeddings:
        if len(embedding) != settings.embedding_dimensions:
            raise EmbeddingProviderError(
                "Embedding dimension mismatch. "
                f"Expected {settings.embedding_dimensions}, got {len(embedding)}."
            )

    return embeddings


def embed_documents(texts: list[str]) -> list[list[float]]:
    return _request_embeddings(texts, task="retrieval.passage")


def embed_query(text: str) -> list[float]:
    return _request_embeddings([text], task="retrieval.query")[0]
