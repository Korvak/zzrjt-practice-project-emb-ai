import requests

def sentiment_analyzer(text_to_analyse):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    Headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = jsonObj, headers=Headers)
    return response.text