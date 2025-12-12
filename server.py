from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    formatted_response = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }
    if response.get('dominant_emotion') == None:
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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)