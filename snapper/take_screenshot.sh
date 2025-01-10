#!/bin/bash

# Directory to save screenshots
SAVE_DIR="memory"

# Read filename format from config.txt
FILENAME_FORMAT=$(grep 'filename_format' config.txt | cut -d '=' -f2)

# Filename with timestamp
FILENAME=$(date +"$FILENAME_FORMAT")

# Full path to save the screenshot
FILEPATH="$SAVE_DIR/$FILENAME"

# Take the screenshot using grim
grim "$FILEPATH"

# Print a message
echo "Screenshot taken and saved as $FILEPATH"
