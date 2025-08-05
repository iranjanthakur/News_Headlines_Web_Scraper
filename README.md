# News Headlines Web Scraper 📰

A Python web scraper designed to extract news headlines from various news websites and save them to a text file. This project demonstrates fundamental web scraping concepts using Python, requests, and BeautifulSoup.

## 🎯 Project Overview

This web scraper was developed as part of a Python Developer Internship (Task 3) to automate data collection from public news websites. It extracts top headlines and saves them in a structured text format for further analysis or reading.

## ✨ Features

- **Multi-site Support**: Works with various news websites
- **Smart Extraction**: Identifies headlines from multiple HTML elements (h1, h2, h3, title tags)
- **Duplicate Removal**: Automatically removes duplicate headlines
- **File Export**: Saves headlines to a timestamped text file
- **Error Handling**: Robust error handling for network issues and parsing errors
- **User-Friendly**: Interactive interface with multiple news site options
- **Respectful Scraping**: Includes proper User-Agent headers and request delays

## 🛠️ Technologies Used

- **Python 3.7+**
- **requests**: For making HTTP requests
- **BeautifulSoup4**: For HTML parsing and data extraction
- **time**: For timestamps and delays

## 📋 Requirements

Before running the scraper, ensure you have the following installed:

```bash
pip install requests beautifulsoup4
```

## 🚀 Installation & Setup

1. **Clone or download the script**
   ```bash
   # Save the news_scraper.py file to your desired directory
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individually:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the scraper**
   ```bash
   python news_scraper.py
   ```

## 💻 Usage

### Basic Usage

Run the script and follow the interactive prompts:

```bash
python news_scraper.py
```

The script will:
1. Display available news sites
2. Allow you to choose a site or enter a custom URL
3. Scrape headlines from the selected site
4. Save results to `headlines.txt`

### Advanced Usage

You can also use the scraper programmatically:

```python
from news_scraper import scrape_news_headlines

# Scrape headlines from a specific URL
headlines = scrape_news_headlines("https://www.bbc.com/news", "custom_output.txt")

# Print the headlines
for i, headline in enumerate(headlines, 1):
    print(f"{i}. {headline}")
```

## 📂 Output Format

The scraper generates a text file with the following format:

```
News Headlines scraped from: https://www.bbc.com/news
Scraped on: 2025-08-05 14:30:25
============================================================

1. Breaking: Major international summit concludes
2. Technology advances reshape global markets
3. Climate change initiatives gain momentum
...
```

## 🌐 Supported News Sites

The scraper works with most news websites, including:

- **BBC News** (https://www.bbc.com/news)
- **Reuters** (https://www.reuters.com)
- **Hacker News** (https://news.ycombinator.com)
- **Custom URLs** (any news website)

## 🔧 Configuration Options

### Customizing Output

- **Change output filename**: Modify the `output_file` parameter
- **Adjust headline limit**: Change the slice value in `top_headlines = unique_headlines[:20]`
- **Add more selectors**: Extend the `title_selectors` list for better headline detection

### Headers Customization

The script uses a realistic User-Agent header to avoid being blocked:

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

## ⚠️ Important Notes

### Legal and Ethical Considerations

- **Respect robots.txt**: Always check a website's robots.txt file before scraping
- **Rate limiting**: The script includes delays to avoid overwhelming servers
- **Terms of service**: Ensure your usage complies with each website's terms
- **Copyright**: Be mindful of copyright when using scraped content

### Technical Limitations

- **Dynamic content**: May not capture JavaScript-generated headlines
- **Anti-bot measures**: Some sites may block automated requests
- **Structure changes**: Website updates may affect scraping accuracy

## 🐛 Troubleshooting

### Common Issues

1. **No headlines found**
   - Website structure may be different
   - Try a different news site
   - Check your internet connection

2. **Request blocked**
   - Site may have anti-bot protection
   - Try adding delays between requests
   - Use different User-Agent strings

3. **Import errors**
   - Ensure all dependencies are installed
   - Check Python version compatibility

### Error Messages

- `Error fetching the webpage`: Network or URL issues
- `An error occurred`: General parsing or file writing errors
- `Invalid choice`: Input validation errors

## 📚 Learning Outcomes

This project demonstrates key concepts:

- **HTTP Requests**: Making GET requests to fetch web content
- **HTML Parsing**: Using BeautifulSoup to navigate DOM structure
- **Data Extraction**: Identifying and extracting specific content
- **File I/O**: Writing structured data to files
- **Error Handling**: Managing network and parsing exceptions
- **Web Scraping Ethics**: Responsible scraping practices

## 🔄 Future Enhancements

Potential improvements:
- Add support for JavaScript-rendered content
- Implement database storage
- Create a web interface
- Add RSS feed parsing
- Include sentiment analysis
- Support for multiple languages

## 📝 Interview Preparation

### Key Questions Covered

1. **What is a GET request?**
   - HTTP method to retrieve data from servers

2. **How to install external packages?**
   - Use `pip install package-name`

3. **What is User-Agent in HTTP?**
   - Header identifying the client application

4. **What is soup.find_all() used for?**
   - Finds all HTML elements matching criteria

5. **Web scraping risks?**
   - Legal issues, rate limiting, blocking, structure changes

## 📄 License

This project is created for educational purposes as part of a Python Developer Internship program.

## 🤝 Contributing

Feel free to fork this project and submit improvements via pull requests.

## 📞 Support

For questions or issues:
- Review the troubleshooting section
- Check the error messages for specific guidance
- Ensure all dependencies are properly installed

---

**Happy Scraping! 🚀**
