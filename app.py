
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.form.get('review', '').strip()

    if not review:
        return render_template(
            'index.html',
            error="Please enter your review."
        )

    blob = TextBlob(review)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.2:
        decision = "Positive"
        emoji = "😊"
        rating = 5
        text_color = "green"
        bg_color = "#d4edda"

    elif sentiment_score < -0.2:
        decision = "Negative"
        emoji = "😞"
        rating = 1
        text_color = "red"
        bg_color = "#f8d7da"

    else:
        decision = "Neutral"
        emoji = "😐"
        rating = 3
        text_color = "#ff9800"
        bg_color = "#fff3cd"

    return render_template(
        'result.html',
        review=review,
        decision=decision,
        emoji=emoji,
        rating=rating,
        score=sentiment_score,
        text_color=text_color,
        bg_color=bg_color
    )


if __name__ == '__main__':
    app.run(debug=True)
