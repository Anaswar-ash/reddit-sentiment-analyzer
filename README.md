Reddit Sentiment Analyzer.
Author: Ash.
A web application built with Python and Flask that performs a weighted sentiment analysis on any given topic by fetching and analyzing posts and comments from Reddit.

📝 Overview
This project provides a more accurate and nuanced view of public opinion on Reddit than a simple title analysis. It fetches not only post titles but also the post's main content (selftext) and the top-voted comments for each thread.

The core of the application is its weighted scoring algorithm, which gives more influence to highly upvoted posts and comments. This ensures the final sentiment score better reflects the community's consensus rather than a simple, unweighted average.

✨ Key Features
Deep Content Analysis: Analyzes post titles, post bodies, and top comments.

Weighted Sentiment Scoring: Uses upvotes as a weight to provide a more representative sentiment score.

VADER Sentiment Engine: Utilizes the VADER library, which is specifically attuned to sentiments expressed on social media.

Simple Web Interface: A clean and straightforward UI to enter a topic and view the detailed results.

Comprehensive Results: Displays an overall sentiment, a precise compound score, and a percentage breakdown of positive, neutral, and negative content.

⚙️ How It Works
The application follows a simple but powerful logic flow:

Data Fetching: The user enters a topic, which is used to search r/all via the PRAW (Python Reddit API Wrapper) library. The app fetches the top posts related to the topic.

Content Aggregation: For each post, the app extracts the title, the selftext (if it exists), and the top-voted comments.

Sentiment Scoring: Each piece of text (title, body, comment) is individually analyzed by the VADER library, which returns a compound sentiment score from -1 (most negative) to +1 (most positive).

Weighted Calculation: The final sentiment score is calculated as a weighted average. The compound score of each text snippet is multiplied by its weight (upvotes + 1, to avoid zero-weight items).

Weighted Score = Σ(compound_score * weight) / Σ(weight)

Results Display: The final weighted score is classified as Positive, Neutral, or Negative and displayed to the user along with detailed statistics.

🛠️ Technology Stack
Backend: Python, Flask

Reddit API Wrapper: PRAW

Sentiment Analysis: VADER (vaderSentiment)

Environment Management: python-dotenv

Frontend: HTML (with a simple, clean interface)

🚀 Getting Started
Follow these instructions to get a local copy up and running.

Prerequisites
Python 3.9+

A Reddit account

1. Clone the Repository
git clone [https://github.com/your-username/reddit-sentiment-analyzer.git](https://github.com/your-username/reddit-sentiment-analyzer.git)
cd reddit-sentiment-analyzer

2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

4. Set Up Reddit API Credentials
This is a critical step. The application will not work without valid Reddit API credentials.

Create a Reddit Application:

Go to Reddit's apps page.

Scroll to the bottom and click "are you a developer? create an app...".

Fill out the form:

name: A unique name for your app (e.g., MySentimentAnalyzer).

type: Select script.

redirect uri: Use http://localhost:8080 (this is required but won't be used).

Click "create app".

Create a .env file:

In the root directory of the project, create a file named .env.

Copy your credentials into this file. Your client_id is under the app name, and your secret is next to the "secret" field.

# .env
REDDIT_CLIENT_ID="YOUR_CLIENT_ID_HERE"
REDDIT_CLIENT_SECRET="YOUR_CLIENT_SECRET_HERE"
REDDIT_USER_AGENT="SentimentWebApp/0.1 by u/YourUsername"

5. Run the Application
Once your environment is set up, start the Flask server.

python app.py

Open your web browser and navigate to http://127.0.0.1:5000 to use the application.

⚠️ Disclaimer
This is a technical project designed to demonstrate data aggregation and NLP techniques. It is not intended as a financial or trading tool. The sentiment analysis is based on a specific algorithm and a limited sample of data and should be interpreted as a high-level summary, not as definitive advice.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
=======
Author: Ash.
>>>>>>> 4718ec403f7862e3842db53e8511201b7823a37c
