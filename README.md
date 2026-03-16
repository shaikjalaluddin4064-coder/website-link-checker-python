# website-link-checker-python
# Automotive Website Link Checker

This project is a Python-based QA automation script designed to detect broken links on automotive websites.

The tool scans all links from a webpage and verifies whether they return valid HTTP responses.

## Target Website

For demonstration purposes, the script analyzes links from:

https://www.peugeot.com/en/

This simulates a real-world QA testing scenario for automotive brand websites.

## Technologies Used

- Python
- Requests
- BeautifulSoup

## Features

- Extracts all links from the webpage
- Converts relative links into absolute URLs
- Checks HTTP status codes
- Identifies broken or inaccessible links
- Prevents duplicate checks

## How to Run

1. Install dependencies
