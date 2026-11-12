-- Cloudflare D1 schema for the timeline guestbook.
-- Apply in the dashboard (D1 > your database > Console) or with:
--   npx wrangler d1 execute portfolio-db --remote --file=schema.sql
CREATE TABLE IF NOT EXISTS timeline_post (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    content    TEXT NOT NULL,
    created_at TEXT NOT NULL
);
