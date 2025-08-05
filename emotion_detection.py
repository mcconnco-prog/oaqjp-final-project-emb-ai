import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers = headers, json = myobj)
    json_response = json.loads(response.text) 
    emotion_data = json_response['emotionPredictions'][0]
    
    anger = emotion_data['emotion']['anger']
    disgust = emotion_data['emotion']['disgust']
    fear = emotion_data['emotion']['fear']    
    joy = emotion_data['emotion']['joy']
    sadness = emotion_data['emotion']['sadness']

    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy':joy,
        "sadness": sadness,
    }

    dominant_emotion = max(emotions, key= emotions.get)

    return {'anger': anger, 
    'disgust': disgust,
    'fear': fear,
    'joy': joy, 
    'sadness': sadness, 
    "dominant emotion": dominant_emotion}