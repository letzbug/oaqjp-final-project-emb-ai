"""
Flask web server for the Emotion Detection application.
This module provides the backend API and serves the frontend.
"""

from flask import Flask, render_template, request, jsonify

# Import the emotion detection function from our package
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """Render the main emotion detector homepage."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Process emotion detection request with input validation."""
    text = request.json.get('text') if request.json else None

    # Validate input
    if not text or not str(text).strip():
        return jsonify({
            'status_code': 400,
            'error': 'Invalid input. Text cannot be empty.'
        }), 400

    # Get emotion analysis
    result = emotion_detector(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
