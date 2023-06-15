import urllib.request
import json
import os
import ssl
import gradio as gr
import plotly.express as px
# import matplotlib.pyplot as plt
import pandas as pd

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

description = "문장을 입력하면 긍정문인지, 부정문인지 판단합니다."
title = "긍정, 부정문 판독기"

def predict(text):
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data = {"inputs": text}

    body = str.encode(json.dumps(data))

    url = 'https://distilbert-base-uncase-s9desgx4.eastus.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = ' '
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key),
               'azureml-model-deployment': 'main'}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        result = json.loads(result.decode('utf-8'))[0]
        # print(result, type(result), json.loads(result.decode('utf-8'))[0]['label'])

        # prepare some data
        if result['label'] == "POSITIVE":
            x = ["POSITIVE", "NEGATIVE"]
        else:
            x = ["NEGATIVE", "POSITIVE"]
        y = [result['score'], 1 - result['score']]
        data = pd.DataFrame()
        data['Subject'] = y
        data['Percentage'] = x
        # create a new plot
        p = px.bar(data, x='Subject', y='Percentage', orientation='h')

        return p

        # Using Matplotlib
        # prepare some data
        # if result['label'] == "POSITIVE":
        #     x = ["POSITIVE", "NEGATIVE"]
        # else:
        #     x = ["NEGATIVE", "POSITIVE"]
        # y = [result['score'], 1 - result['score']]
        # print(y)
        # # create a new plot
        # # plt.rcParams['figure.figsize'] = 2, 2
        # # fig = plt.figure()
        # # ax = fig.add_axes([0, 0, 1, 1])
        # # ax.bar(x, y)
        # # plt.title("Marks per subject")
        # # plt.xlabel("Subject")
        # # plt.ylabel("Score")
        #
        # plt.barh(x, y)
        # plt.show()
        #
        # return plt

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


iface = gr.Interface(
    fn=predict,
    inputs='text',
    outputs='plot',
    description=description,
    title=title,
    examples=[["안녕하세요"]]
)

iface.launch(share=False)
