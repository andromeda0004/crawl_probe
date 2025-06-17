````markdown
# Recursive Web Spider in Python

This project is a simple recursive web spider built using Python. It takes a base URL and a keyword, then crawls all reachable links from the starting page. If a link matches the given keyword, it is printed separately.

## Features

- Recursive crawling using depth-first search
- Avoids revisiting links
- Handles request failures with retry logic
- Timeout protection for slow/unreachable sites
- Keyword-based filtering of matched URLs

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4`

You can install the required libraries using:

```bash
pip install requests beautifulsoup4
````

## How to Use

1. Clone or copy the script to your local machine.
2. Run the script:

   ```bash
   python spider.py
   ```
3. Enter the URL and keyword when prompted.

### Example

* **URL**: `https://books.toscrape.com/index.html`
* **Keyword**: `catalogue`

The script will begin crawling all reachable links and print out:

* Every link it visits depth first
* Links that contain the specified keyword

## Notes

* The spider only works with HTTP/HTTPS links.
* Avoid using this script to crawl websites without permission.
* It's recommended to use this on static, educational websites like `books.toscrape.com`.

## Limitations

* No support for robots.txt parsing (ethical crawling not enforced)
* No rate limiting or maximum depth/count control
* Only filters based on presence of keyword in the URL, not page content

