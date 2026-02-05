from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector', methods=['GET'])
def detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Error: 'textToAnalyze' parameter is required.", 400

    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
