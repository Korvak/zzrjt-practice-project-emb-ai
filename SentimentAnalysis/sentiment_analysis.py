import requests
import json 

def sentiment_analyzer(text_to_analyse):
    try :
        URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
        Headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
        jsonObj = { "raw_document": { "text": text_to_analyse } }
        response = requests.post(URL, json = jsonObj, headers=Headers)
        formatted_response = json.loads(response.text)
        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        # Returning a dictionary containing sentiment analysis results
        return {'label': label, 'score': score}
    except Exception as e:
        print(e)
        return {"error" : str(e)}