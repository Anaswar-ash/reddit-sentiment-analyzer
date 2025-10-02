# Technical Documentation - Reddit Sentiment Analyzer
Author: Ash.
## 1. Project Overview

This project is a web application built with Python and Flask that analyzes the sentiment of Reddit posts based on a user-provided topic. It fetches data from Reddit using the PRAW library, performs sentiment analysis using the VADER library, and displays the results on a user-friendly web page styled with Bootstrap.

## 2. Project Structure

```
reddit-sentiment-analyzer/
├── .gitignore
├── app.py
├── requirements.txt
├── docs/
│   └── TECHNICAL_DOCUMENTATION.md
└── templates/
    └── index.html
```

- **`app.py`**: The core Flask application. It handles web routes, form submissions, and the main logic for interacting with the Reddit API and performing sentiment analysis.
- **`requirements.txt`**: Lists the necessary Python packages for the project.
- **`templates/index.html`**: The HTML template for the user interface.
- **`docs/TECHNICAL_DOCUMENTATION.md`**: This file.

## 3. Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository (if applicable).**

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Reddit API Credentials:**
   - Create a file named `.env` in the root directory.
   - Add your Reddit API credentials to this file in the following format:
     ```
     REDDIT_CLIENT_ID=your_client_id
     REDDIT_CLIENT_SECRET=your_client_secret
     REDDIT_USER_AGENT=your_user_agent
     ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## 4. Acquiring Reddit API Credentials

To use the Reddit API, you need to create a new "script" application on Reddit.

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
2. Scroll to the bottom and click "are you a developer? create an app...".
3. Fill out the form:
   - **name**: A name for your app (e.g., `SentimentAnalyzer`).
   - **type**: Select `script`.
   - **description**: An optional description.
   - **about url**: Can be left blank.
   - **redirect uri**: Use `http://localhost:8080` (this is required for script apps but won't be used by our app).
4. Click "create app".
5. You will now see your app's credentials.
   - The **`client_id`** is the string of characters under "personal use script".
   - The **`client_secret`** is the string next to "secret".
   - For the **`user_agent`**, you can use a descriptive string, for example: `MySentimentAnalyzer/0.1 by u/YourUsername`.

Add these three values to your `.env` file as described in the setup instructions.
