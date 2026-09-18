from app.services.chunking_service import split_text


def test_split_text_returns_single_chunk_for_short_text() -> None:
    chunks = split_text("Short business document.", chunk_size=100, chunk_overlap=10)
    assert chunks == ["Short business document."]


def test_split_text_creates_overlapping_chunks() -> None:
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chunks = split_text(text, chunk_size=10, chunk_overlap=2)

    assert len(chunks) > 1
    assert chunks[0][-2:] == chunks[1][:2]


def test_split_text_rejects_invalid_overlap() -> None:
    try:
        split_text("abc", chunk_size=10, chunk_overlap=10)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
