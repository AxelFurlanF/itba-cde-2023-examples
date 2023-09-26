#!/bin/bash

# Start PostgreSQL service
brew services start postgresql

# Wait a moment to ensure the service has fully started
sleep 5

# Create a new PostgreSQL database
createdb itba-dev

psql -d itba-dev -f titanic.sql
