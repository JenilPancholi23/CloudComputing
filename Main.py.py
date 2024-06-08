#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Specify the AWS region for Canada Central
region_name = 'ca-central-1'

# Initialize AWS Comprehend client with the specified region
comprehend = boto3.client('comprehend', region_name=region_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None  # Initialize sentiment outside the if block
    if request.method == 'POST':
        text = request.form['text']
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment_scores = response['SentimentScore']
        max_score = max(sentiment_scores.values())
        sentiment = 'Positive' if sentiment_scores['Positive'] == max_score else \
                    'Negative' if sentiment_scores['Negative'] == max_score else \
                    'Neutral' if sentiment_scores['Neutral'] == max_score else 'Mixed'
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


# In[ ]:




