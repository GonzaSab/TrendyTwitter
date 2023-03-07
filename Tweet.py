import pandas as pd
from pytrends.request import TrendReq
import random
import openai
import os
import requests
from requests.structures import CaseInsensitiveDict
import json

def get_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response.choices and response.choices[0].text:
        answer = response.choices[0].text.strip()
    else:
        answer = "No valid response received from OpenAI API"
        
    return answer

pytrend = TrendReq()

#Get todays trending
df = pytrend.trending_searches()
df.head()
arr= df.values

random_number = random.randint(0, 19)
print("All trends: \n {} \n".format(arr)) #Array con todos los trends
print("Selected trend: {} \n".format(arr[random_number][0])); #Elemento 1

# Set the keyword you want to search for
keyword = arr[random_number][0]

# Build the payload
pytrend.build_payload(kw_list=[keyword])

# Get related queries
related_queries = pytrend.related_queries()[keyword]['top']

titles=[]
# Print the most searched titles for the keyword
#print("Most searched titles for", keyword)
for title in related_queries['query']:
    titles.append(title)


print ("Most searched titles: \n{} \n".format(titles))

api_key = "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"
openai.api_key = api_key

try:
    text_response = get_text("Write me a 256 characters parragraph about {} asuming is 2023 and if these are the lastest trending searches in the web: {}".format(arr[random_number][0], titles))
    # Print the answer
    print("Generated text using titles: \n{} \n".format(text_response))

except Exception as e:
    # Handle any exceptions that occur during the API request
    print("Error: {}".format(str(e)))

try:
    text_response2 = get_text("Resume this parragraph '{}' using between 100 and 120 characters in a tweet format".format(text_response))
    # Print the answer
    print("Final Tweet: \n{}".format(text_response2))

except Exception as e:
    # Handle any exceptions that occur during the API request
    print("Error: {}".format(str(e)))