#!/bin/bash

echo "Dirsearch Auto Scanner"

read -p "Enter Target URL: " TARGET

if [ -z "$TARGET" ]; then
    echo "No target!"
    exit 1
fi

if ! command -v dirsearch &> /dev/null
then
    echo "Installing dirsearch..."
    git clone https://github.com/maurosoria/dirsearch.git
    cd dirsearch
    python3 dirsearch.py -u $TARGET
else
    dirsearch -u $TARGET
fi
