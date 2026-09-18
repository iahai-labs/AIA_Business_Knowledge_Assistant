docker compose exec db psql -U aia -d aia_knowledge -c "DROP TABLE IF EXISTS document_chunks;"
