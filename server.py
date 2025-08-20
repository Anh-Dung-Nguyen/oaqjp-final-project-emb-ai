"""
This module contains the Flask web server for the emotion detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    """
    Renders the index.html page for the web application.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=['POST'])
def emotion_detect_route():
    """
    This function handles the POST request for emotion detection.
    It takes text from the form, calls the emotion_detector function,
    and returns a formatted string response.
    """
    text_to_analyze = request.form['textToAnalyze']
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_output = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return formatted_output

if __name__ == '__main__':
    app.run(debug=True)