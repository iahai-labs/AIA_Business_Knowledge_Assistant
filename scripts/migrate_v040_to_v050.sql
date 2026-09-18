BEGIN;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(320) NOT NULL UNIQUE,
    password_hash VARCHAR(512) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_users_id ON users (id);
CREATE UNIQUE INDEX IF NOT EXISTS ix_users_email ON users (email);

ALTER TABLE documents
    ADD COLUMN IF NOT EXISTS owner_user_id INTEGER NULL;

CREATE INDEX IF NOT EXISTS ix_documents_owner_user_id
    ON documents (owner_user_id);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'documents_owner_user_id_fkey'
    ) THEN
        ALTER TABLE documents
            ADD CONSTRAINT documents_owner_user_id_fkey
            FOREIGN KEY (owner_user_id)
            REFERENCES users(id)
            ON DELETE CASCADE;
    END IF;
END $$;

ALTER TABLE conversations
    ADD COLUMN IF NOT EXISTS owner_user_id INTEGER NULL;

CREATE INDEX IF NOT EXISTS ix_conversations_owner_user_id
    ON conversations (owner_user_id);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'conversations_owner_user_id_fkey'
    ) THEN
        ALTER TABLE conversations
            ADD CONSTRAINT conversations_owner_user_id_fkey
            FOREIGN KEY (owner_user_id)
            REFERENCES users(id)
            ON DELETE CASCADE;
    END IF;
END $$;

COMMIT;
