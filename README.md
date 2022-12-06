To use the text scraping utility, follow these steps:

Install the required dependencies by running pip install -r requirements.txt in your command line.

Use the check_and_run.py script to check if the required dependencies are installed and, if not, to install them. You can run this script by typing python check_and_run.py in your command line.

Use the scraper.py script to scrape text from a file. You can run this script by typing python scraper.py <filepath>, where <filepath> is the path to the file you want to scrape text from.

The scraped text will be printed to the console. You can redirect the output to a file by using the > operator, like this: python scraper.py <filepath> > output.txt.

The scraper.py script supports the following file types:

HTML
DOCX
PDF
XLSX
CSV
TXT
If you need to use a proxy to download dependencies, you can specify the proxy URL by using the --proxy option when running the check_and_run.py script, like this: python check_and_run.py --proxy http://<proxy_url>:<port>.