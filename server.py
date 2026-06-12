from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text = request.json.get('text')
    
    # Improved Error Handling for blank input
    if not text or not str(text).strip():
        return jsonify({
            'status_code': 400,
            'error': 'Invalid input. Text cannot be empty.'
        }), 400
    
    result = emotion_detector(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)