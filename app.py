from flask import Flask, render_template, request
from newspaper import Article
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai

# Your OpenAI API Key (Make sure it's set as an environment variable or passed directly)
openai.api_key = "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"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tweet = None
    if request.method == 'POST':
        url = request.form['urlInput']
        
        # Step 1: Scrape the article
        article = Article(url)
        article.download()
        article.parse()
        content = article.text
        
        # Step 2: Initialize OpenAI model
        llm = ChatOpenAI(temperature=0.7, openai_api_key=openai.api_key)

        # Step 3: Define your summarization prompt
        summary_prompt = """
        Summarize the following article in a concise way suitable for a tweet:
        {article_text}
        """
        summary_template = PromptTemplate(input_variables=["article_text"], template=summary_prompt)
        summary_chain = LLMChain(llm=llm, prompt=summary_template)

        # Step 4: Generate a summary
        summary = summary_chain.run(content)

        # Step 5: Define your tweet generation prompt
        tweet_prompt = """
        Write a tweet about the following summary:
        {summary}
        """
        tweet_template = PromptTemplate(input_variables=["summary"], template=tweet_prompt)
        tweet_chain = LLMChain(llm=llm, prompt=tweet_template)

        # Step 6: Generate the tweet
        tweet = tweet_chain.run(summary)

        # Step 7: Post-process the tweet for replacements
        tweet = tweet.replace('Upsun', '@upsuncom')
        tweet = tweet.replace('Platform.sh', 'https://platform.sh/')
        tweet = tweet.replace('Platform', 'https://platform.sh/')
        
    return render_template('index.html', tweet=tweet)

if __name__ == '__main__':
    app.run(debug=True)
