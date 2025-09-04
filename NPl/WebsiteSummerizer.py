import google.generativeai as genai
from newspaper import Article

# Gemini API setup
genai.configure(api_key="AIzaSyDE4bcU2PVGQG_11Hp9z7nAQntDYEc98D8")
model = genai.GenerativeModel("gemini-2.5-flash")

def scrape_website_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error fetching content: {str(e)}"

def summarize_with_gemini(content):
    prompt = f"Summarize the following website content in simple points:{content}"
    response = model.generate_content(prompt)
    return response.text

# Main driver
if __name__ == "__main__":
    url = input("Enter the website URL: ")
    content = scrape_website_content(url)
    if "Error" in content:
        print(content)
    else:
        print("Website Content Summary:")
        summary = summarize_with_gemini(content)
        print(summary)


