#!/bin/sh

# Run alembic migrations
alembic upgrade head

# Start the server
uvicorn main:app --host 0.0.0.0 --port 6800 --reload