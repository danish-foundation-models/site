#!/usr/bin/env bash
set -e
OUTFILE="scripts/tailwindcss"
if [ ! -f "$OUTFILE" ]; then
  echo "INFO: 'tailwindcss' not found. Attempting to download..."
  OS="$(uname -s)"
  ARCH="$(uname -m)"
  case "$OS" in
    Linux) PLATFORM="linux" ;;
    Darwin) PLATFORM="macos" ;;
    MINGW*|MSYS*|CYGWIN*|Windows_NT) PLATFORM="windows" ;;
    *) echo "ERROR: Unsupported OS: $OS"; exit 1 ;;
  esac
  case "$ARCH" in
    x86_64|amd64) ARCH="x64" ;;
    arm64|aarch64) ARCH="arm64" ;;
    *) echo "ERROR: Unsupported architecture: $ARCH"; exit 1 ;;
  esac
  FILENAME="tailwindcss-${PLATFORM}-${ARCH}"
  URL="https://github.com/tailwindlabs/tailwindcss/releases/latest/download/${FILENAME}"
  echo "INFO: Downloading Tailwind CSS CLI from:"
  echo "$URL"
  curl -L -o "$OUTFILE" "$URL"
  if [ "$PLATFORM" != "windows" ]; then chmod +x "$OUTFILE"; fi
else
  echo "INFO: 'tailwindcss' already exists. Skipping download."
fi
if [ -f "$OUTFILE" ]; then
  echo "INFO: Running Tailwind CSS CLI..."
  $OUTFILE --input scripts/landing.css --output landing/css/index.css --verbose $@
else
  echo "ERROR: Failed to obtain 'tailwindcss' CLI."
  exit 1
fi
