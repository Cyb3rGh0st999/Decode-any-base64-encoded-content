# Decode-any-base64-encoded-content


This Python script provides a simple GUI to read `.eml` and `.txt` files. It can parse and decode any base64-encoded content (especially XML files) from `.eml` files and display both the original encoded content and the decoded version. Users can also export the parsed content to a text file.

## Features

- **Supports `.eml` and `.txt` files**:
  - Reads both `.eml` (email files) and regular `.txt` files.
  - Displays the original content and decodes any base64-encoded content (especially useful for XML attachments in `.eml` files).
  
- **Base64 Decoding**:
  - Automatically detects base64-encoded content in `.eml` files and decodes it.
  - Displays both the original encoded and decoded content for clarity.

- **XML File Detection**:
  - Identifies XML files within `.eml` files and processes them for base64 decoding.
  - Displays the filename and the decoded content if base64 encoded.

- **Export Functionality**:
  - Export the parsed output (including both original and decoded content) to a `.txt` file.

## Requirements

- **Python 3.x**
- **tkinter library** (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/eml-parser
   cd eml-parser
