# import gradio as gr
#
# description = "Story generation with GPT-2"
# title = "Generate your own story"
# examples = [["Adventurer is approached by a mysterious stranger in the tavern for a new quest."]]
#
# interface = gr.Interface.load("huggingface/pranavpsv/gpt2-genre-story-generator",
#             description=description,
#             examples=examples
# )
#
# interface.launch()

import gradio as gr
description = "BigGAN text-to-image demo."
title = "BigGAN ImageNet"
interface = gr.load("huggingface/distilbert-base-uncased-finetuned-sst-2-english",
            description=description,
            title = title,
            examples=[["american robin"]],
            inputs="text",
            outputs="text"
)
interface.launch()

# def greet(name):
#     return "Hello " + name + "!"
#
# demo = gr.Interface(fn=greet, inputs="text", outputs="text", description=description, examples=examples, title=title)
#
# demo.launch()

# import gradio as gr
#
# from transformers import pipeline
#
# pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
#
# def predict(text):
#   return pipe(text)[0]["translation_text"]
#
# iface = gr.Interface(
#   fn=predict,
#   inputs='text',
#   outputs='text',
#   examples=[["Hello! My name is Omar"]]
# )
#
# iface.launch()