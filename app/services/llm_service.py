import httpx

from app.core.config import settings


class LLMProviderError(RuntimeError):
    pass


def generate_grounded_answer(
    question: str,
    context: str,
) -> str:
    if not settings.groq_api_key:
        raise LLMProviderError(
            "GROQ_API_KEY is not configured. Add it to .env before asking questions."
        )

    url = f"{settings.groq_base_url.rstrip('/')}/chat/completions"

    system_prompt = (
        "You are a business knowledge assistant. "
        "Answer only from the provided context. "
        "Do not use outside knowledge. "
        "If the context does not contain enough information, say: "
        "\"I don't have enough information in the indexed documents to answer that.\" "
        "Cite sources inline using ONLY the exact reference format [1], [2], [3]. "
        "When using information from a source, cite it inline with the provided "
        "reference marker such as [1] or [2]. "
        "Use only reference numbers that appear in the provided context. "
        "Do not invent citations."
    )

    payload = {
        "model": settings.groq_model,
        "temperature": settings.answer_temperature,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": (
                    f"QUESTION:\n{question}\n\n"
                    f"CONTEXT:\n{context}"
                ),
            },
        ],
    }

    headers = {
        "Authorization": f"Bearer {settings.groq_api_key}",
        "Content-Type": "application/json",
    }

    try:
        with httpx.Client(timeout=settings.groq_timeout_seconds) as client:
            response = client.post(
                url,
                headers=headers,
                json=payload,
            )
            response.raise_for_status()

    except httpx.HTTPStatusError as exc:
        body = exc.response.text[:1000]
        raise LLMProviderError(
            f"Groq API returned HTTP {exc.response.status_code}: {body}"
        ) from exc

    except httpx.HTTPError as exc:
        raise LLMProviderError(
            f"Could not connect to Groq API: {exc}"
        ) from exc

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError, AttributeError) as exc:
        raise LLMProviderError(
            "Groq API returned an unexpected response payload."
        ) from exc