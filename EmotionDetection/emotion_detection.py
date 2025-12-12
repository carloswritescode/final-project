import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=15)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    formatted_emotions = {}
    for emotion in emotions:
        score = emotions.get(emotion, 0)
        formatted_emotions[emotion] = score


    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = formatted_emotions[dominant_emotion]

    return emotions, dominant_emotion, dominant_score