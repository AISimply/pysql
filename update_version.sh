#!/bin/bash

VERSION_FILE="VERSION"

# Read the current version
if [ ! -f "$VERSION_FILE" ]; then
    echo "0.0.0" > "$VERSION_FILE"
fi
CURRENT_VERSION=$(cat "$VERSION_FILE")

# Split version into components
IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

# Increment PATCH version by default
PATCH=$((PATCH + 1))

# Assemble new version
NEW_VERSION="$MAJOR.$MINOR.$PATCH"

# Update the VERSION file
echo "$NEW_VERSION" > "$VERSION_FILE"

echo "Updated version: $NEW_VERSION"