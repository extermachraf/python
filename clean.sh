#!/bin/bash

# This script removes all __pycache__ directories recursively from the project directory

ROOT_DIR="$(pwd)"

echo "Searching and removing all '__pycache__' folders inside $ROOT_DIR"

find "$ROOT_DIR" -type d -name "__pycache__" -exec echo "Removing {}" \; -exec rm -rf {} +