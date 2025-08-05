'''This file initiates a web app of emotion detector
   which is executed via flask on localhost:5000
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    '''Initiates the emotion detector web app
    '''
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant emotion"]
    if dominant_emotion is None:
        return "Invalid Input! Try Again!"
    return (
    f"anger: {anger}, " 
    f"disgust: {disgust}, " 
    f"fear: {fear}, " 
    f"joy: {joy}, " 
    f"sadness: {sadness}, " 
    f"dominant emotion: {dominant_emotion}" )

@app.route("/", methods=["GET"])
def render_index_page():
    """renders the index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
