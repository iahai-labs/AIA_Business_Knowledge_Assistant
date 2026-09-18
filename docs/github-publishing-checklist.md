# GitHub Publishing Checklist

## Repository

- [ ] working tree clean
- [ ] tag `v1.0.0` created
- [ ] `.env` is not tracked
- [ ] no API keys in Git history
- [ ] README renders correctly
- [ ] Mermaid architecture diagram renders correctly
- [ ] license is present
- [ ] demo files contain no private data

## Verification

- [ ] test suite passes
- [ ] smoke test passes
- [ ] Alembic shows `0001 (head)`
- [ ] Swagger opens in development
- [ ] `/ready` returns 200
- [ ] grounded query succeeds
- [ ] unrelated query returns safe fallback
- [ ] non-admin receives 403 from admin endpoints
- [ ] cross-user ownership isolation verified

## Presentation

- [ ] repository description added
- [ ] repository topics added
- [ ] short demo GIF or screenshots prepared
- [ ] architecture image or Mermaid diagram visible
- [ ] release notes added for v1.0.0
