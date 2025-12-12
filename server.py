from flask import Flask, render_template, request, jsonify
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector(text):
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    emotions = response['emotions']
    dominant_emotion = response['dominant_emotion']

    return f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)