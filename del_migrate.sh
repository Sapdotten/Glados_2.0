#!/bin/bash

# Путь к базе данных
DB_PATH="db.sqlite3"

# Путь к папке с версиями Alembic
VERSIONS_FOLDER="apps/alembic/versions"

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Текущее время
CURRENT_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# Удаление базы данных
if [ -f "$DB_PATH" ]; then
    rm "$DB_PATH"
    echo -e "${GREEN}[$CURRENT_TIME] Database $DB_PATH deleted.${NC}"
else
    echo -e "${YELLOW}[$CURRENT_TIME] Database $DB_PATH does not exist.${NC}"
fi

# Очистка папки с версиями Alembic
if [ -d "$VERSIONS_FOLDER" ]; then
    rm -rf "$VERSIONS_FOLDER"/*
    echo -e "${GREEN}[$CURRENT_TIME] Versions folder $VERSIONS_FOLDER cleared.${NC}"
else
    echo -e "${YELLOW}[$CURRENT_TIME] Versions folder $VERSIONS_FOLDER does not exist.${NC}"
fi