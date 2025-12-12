"""
This is the server file for Emotion Detector app.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Defining emotion_detector.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    formatted_response = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }

    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is: "
        f"anger: {formatted_response['anger']}, "
        f"disgust: {formatted_response['disgust']}, "
        f"fear: {formatted_response['fear']}, "
        f"joy: {formatted_response['joy']}, "
        f"sadness: {formatted_response['sadness']}, "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

@app.route("/", methods=['GET'])
def render_index_page():
    """
    Defining index page template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
