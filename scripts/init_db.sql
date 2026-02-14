-- Initial database setup for OpenLearn AI

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For full-text search

-- Create schemas
CREATE SCHEMA IF NOT EXISTS auth;
CREATE SCHEMA IF NOT EXISTS content;
CREATE SCHEMA IF NOT EXISTS analytics;

-- Grant permissions
GRANT ALL ON SCHEMA auth TO openlearn;
GRANT ALL ON SCHEMA content TO openlearn;
GRANT ALL ON SCHEMA analytics TO openlearn;

COMMIT;
