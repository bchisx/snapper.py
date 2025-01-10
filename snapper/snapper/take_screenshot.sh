#!/bin/bash

# Directory to save screenshots
SAVE_DIR="memory"

# Read filename format from config.txt
FILENAME_FORMAT=$(grep 'filename_format' config.txt | cut -d '=' -f2)

# Filename with timestamp
FILENAME=$(date +"$FILENAME_FORMAT")

# Full path to save the screenshot
FILEPATH="$SAVE_DIR/$FILENAME"

# Check if the system is using X11
if [ "$XDG_SESSION_TYPE" = "x11" ]; then
  # Take the screenshot using maim
  maim "$FILEPATH"
else
  # Take the screenshot using grim
  grim "$FILEPATH"
fi

# Print a message
echo "Screenshot taken and saved as $FILEPATH"
