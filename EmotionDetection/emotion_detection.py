import requests
import json

def emotion_detector(text_to_analyze):
    
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    endpoint = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {
        "raw_document": {"text": text_to_analyze}
    }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(endpoint, json=myobj, headers=headers)
        
        # Handle server errors like 400
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        response_dict = response.json()
        emotions = response_dict["emotionPredictions"][0]["emotion"]
        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    except (requests.RequestException, KeyError, IndexError, ValueError) as e:
        # Handle network errors or unexpected response format
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
