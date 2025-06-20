````markdown
# Recursive Web Spider in Python

This project is a simple recursive web spider built using Python. It takes a base URL and a keyword, then crawls all reachable links from the starting page. If a link matches the given keyword, it is printed separately.

## Features

- Recursive crawling using depth-first search
- Avoids revisiting links
- Handles request failures with retry logic
- Timeout protection for slow or unreachable sites
- Keyword-based filtering of matched URLs

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install the dependencies using:

```bash
pip install requests beautifulsoup4
````

## How to Use

1. Save the script as `spider.py`.

2. Run the script:

   ```bash
   python spider.py
   ```

3. Enter the site URL and keyword when prompted.

### Example

* **URL**: `https://books.toscrape.com/index.html`
* **Keyword**: `catalogue`

The script will:

* Visit each reachable link (depth-first)
* Print URLs containing the keyword separately

## Notes

* The spider works only with HTTP/HTTPS URLs.
* Use this script responsibly. Do not crawl websites without permission.
* Best for static, educational sites (e.g. `books.toscrape.com`).

## Limitations

* Does not parse or respect `robots.txt`
* No built-in rate limiting or max depth control
* Filters only based on keyword presence in the URL, not page content

## Sample Crawl Structure

```
spider(A)
 ├── spider(B)
 │     ├── spider(B1)
 │     └── spider(B2)
 └── spider(C)
```
