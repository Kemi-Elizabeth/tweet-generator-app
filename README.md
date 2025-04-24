# Tweet Generator App

## Description

The **Tweet Generator App** is a web application built with **Flask**, **Langchain**, and **OpenAI** that allows users to generate tweet-worthy summaries from articles. By simply providing a URL to an article, the app scrapes its content, summarizes it, and generates a tweet from the summary.

## Features

- **Article Scraping**: Input a URL, and the app scrapes the article content using `newspaper3k`.
- **Summarization**: Utilizes **Langchain** and **OpenAI** to summarize the article into a concise tweet-friendly format.
- **Tweet Generation**: Generates creative tweets based on the summary of the article.

## Tech Stack

- **Frontend**: 
  - **HTML** and **CSS** for the user interface (UI).
  
- **Backend**: 
  - **Flask** for building the web application.
  - **Langchain** for integrating with OpenAI and generating summaries.
  - **OpenAI API** for AI-powered summarization and tweet generation.

- **Others**:
  - **Python** for the overall development and execution.

## Setup and Installation

### Prerequisites

- **Python 3.12+** (If you're using a virtual environment, it's important to have Python installed)
- **Git** for version control
- **Pip** for package management

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kemi-Elizabeth/tweet-generator-app.git

   ```

### Navigate to the project folder:

```cd tweet-generator-app```

Set up a virtual environment (Optional but recommended):
```python3 -m venv venv```
```source venv/bin/activate   # On macOS/Linux```
```venv\Scripts\activate      # On Windows```
```Install dependencies:```

```pip install -r requirements.txt```

### Set up environment variables:

Create a .env file in the root directory and add your OpenAI API key as follows:

```OPENAI_API_KEY=your_api_key_here```

Run the application:

```flask run```

## How to Use
- Go to the app’s main page.
- Enter the URL of the article you want to summarize into the input field.
- Click the Submit button.
- The app will scrape the article, summarize it, and generate a tweet.

## Contributing
Contributions are welcome to this project! To contribute:

- Fork the repository
- Clone your fork
- Create a new branch (git checkout -b feature-branch)
- Make your changes
- Commit your changes (git commit -am 'Add new feature')
- Push to the branch (git push origin feature-branch)
- Open a pull request on GitHub

## License
This project is licensed under the MIT License - see the LICENSE file for details.



