import os
import praw
from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# --- SETUP ---

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# --- CONSTANTS ---
POST_LIMIT = 25 # Number of posts to fetch
COMMENT_LIMIT = 10 # Number of top comments per post to fetch

# --- INITIALIZATION ---

# Initialize Reddit API client
try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("RED_USER_AGENT", "SentimentAnalysisWebApp/0.1 by YourUsername"),
    )
    # Test the connection
    print(f"Connected to Reddit as: {reddit.user.me()}")
except Exception as e:
    print(f"Error initializing PRAW: {e}")
    reddit = None

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# --- HELPER FUNCTIONS ---

def get_sentiment_compound_score(text):
    """Returns the compound sentiment score from VADER."""
    if not text:
        return 0
    return analyzer.polarity_scores(text)['compound']

def classify_sentiment(compound_score):
    """Classifies a compound score into a sentiment category."""
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# --- FLASK ROUTES ---

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handles the form submission, fetches Reddit data, and performs a weighted sentiment analysis."""
    if not reddit:
        return "Reddit API not configured. Please check your .env file.", 500

    topic = request.form.get('topic')
    if not topic:
        return render_template('index.html', error="Please enter a topic.")

    weighted_scores = []
    analyzed_posts = []
    total_comments_analyzed = 0

    try:
        subreddit = reddit.subreddit("all")
        submissions = subreddit.search(topic, limit=POST_LIMIT)

        for post in submissions:
            # --- Analyze Post Title and Body ---
            title_score = get_sentiment_compound_score(post.title)
            body_score = get_sentiment_compound_score(post.selftext)
            
            # Add post scores to our weighted list. Weight is upvotes + 1 (to avoid zero weight).
            post_weight = post.score + 1
            weighted_scores.append({'score': title_score, 'weight': post_weight})
            if post.selftext: # Only add body score if it exists
                weighted_scores.append({'score': body_score, 'weight': post_weight})

            # --- Analyze Top Comments ---
            post_comments = []
            post.comments.replace_more(limit=0) # Remove "load more comments" links
            
            comment_list = post.comments.list()
            total_comments_analyzed += min(len(comment_list), COMMENT_LIMIT)

            for comment in comment_list[:COMMENT_LIMIT]:
                comment_score = get_sentiment_compound_score(comment.body)
                comment_weight = comment.score + 1
                weighted_scores.append({'score': comment_score, 'weight': comment_weight})
                post_comments.append({
                    'body': comment.body,
                    'author': comment.author.name if comment.author else "[deleted]",
                    'score': comment.score,
                    'sentiment': classify_sentiment(comment_score)
                })

            analyzed_posts.append({
                'title': post.title,
                'url': post.url,
                'score': post.score,
                'sentiment': classify_sentiment(title_score),
                'comments': post_comments
            })

        # --- Calculate Final Weighted Sentiment ---
        if not weighted_scores:
            return render_template('index.html', error=f"No results found for '{topic}'.")

        total_weight = sum(item['weight'] for item in weighted_scores)
        weighted_sum = sum(item['score'] * item['weight'] for item in weighted_scores)
        
        final_compound_score = weighted_sum / total_weight if total_weight > 0 else 0
        overall_sentiment = classify_sentiment(final_compound_score)
        
        # --- Prepare Summary Stats ---
        sentiments = [classify_sentiment(item['score']) for item in weighted_scores]
        positive_percent = round((sentiments.count("Positive") / len(sentiments)) * 100, 1)
        negative_percent = round((sentiments.count("Negative") / len(sentiments)) * 100, 1)
        neutral_percent = round((sentiments.count("Neutral") / len(sentiments)) * 100, 1)
        
        results = {
            'topic': topic,
            'overall_sentiment': overall_sentiment,
            'compound_score': f"{final_compound_score:.2f}",
            'positive_percent': positive_percent,
            'negative_percent': negative_percent,
            'neutral_percent': neutral_percent,
            'post_count': len(analyzed_posts),
            'comment_count': total_comments_analyzed,
            'posts': analyzed_posts
        }
        
        return render_template('index.html', results=results)

    except Exception as e:
        print(f"An error occurred during search: {e}")
        return f"An error occurred while fetching data from Reddit: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)