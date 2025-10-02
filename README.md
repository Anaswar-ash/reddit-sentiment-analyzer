# Reddit Sentiment Analyzer

This is a web application that allows you to search for a topic and analyze the sentiment of related posts on Reddit.

## Features

- **Topic Search:** Enter any keyword to search for relevant posts on Reddit.
- **Sentiment Analysis:** The application analyzes the sentiment of post titles and provides an overall sentiment score (Positive, Negative, or Neutral) for the topic.
- **Top Posts:** View a list of the top related posts, their individual sentiment, and a direct link to the Reddit thread.

## Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

- Python 3.x
- A Reddit account

### Installation

1. **Clone the repository (or download the files).**

2. **Navigate to the project directory:**
   ```bash
   cd reddit-sentiment-analyzer
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Reddit API credentials:**
   - Create a file named `.env` in the root of the project.
   - Add your credentials in the following format:
     ```
     REDDIT_CLIENT_ID=your_client_id
     REDDIT_CLIENT_SECRET=your_client_secret
     REDDIT_USER_AGENT=your_user_agent
     ```
   - For detailed instructions on how to get these credentials, please see the `docs/TECHNICAL_DOCUMENTATION.md` file.

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open your browser** and go to `http://127.0.0.1:5000`.

## Technical Details

For a more in-depth look at the project architecture, setup, and API usage, please refer to the [Technical Documentation](./docs/TECHNICAL_DOCUMENTATION.md).
