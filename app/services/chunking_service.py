from app.core.config import settings


def split_text(
    text: str,
    chunk_size: int | None = None,
    chunk_overlap: int | None = None,
) -> list[str]:
    size = chunk_size or settings.chunk_size
    overlap = chunk_overlap if chunk_overlap is not None else settings.chunk_overlap

    if size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0 or overlap >= size:
        raise ValueError("chunk_overlap must be >= 0 and smaller than chunk_size.")

    normalized = " ".join(text.split())

    if not normalized:
        return []

    if len(normalized) <= size:
        return [normalized]

    chunks: list[str] = []
    start = 0

    while start < len(normalized):
        end = min(start + size, len(normalized))
        chunk = normalized[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(normalized):
            break

        start = end - overlap

    return chunks
