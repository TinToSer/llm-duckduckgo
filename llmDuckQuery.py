#JMS
#Developed by https://github.com/tintoser

# A lot of thanks to duck.ai, an initiative by duckduckgo search engine, by birth this search engine is known for its privacy and zero tracking

import requests
import re


def queryDuck(prompt):
    url = "https://duckduckgo.com:443/duckchat/v1/status"
    headers = {"Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"", "Cache-Control": "no-store", "Accept-Language": "en-US", "Sec-Ch-Ua-Mobile": "?0", "X-Vqd-Accept": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://duckduckgo.com/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=1, i"}
    retn=requests.get(url, headers=headers)
    url = "https://duckduckgo.com:443/duckchat/v1/chat"
    headers = {"Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"", "Accept-Language": "en-US", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36", "Content-Type": "application/json", "Accept": "text/event-stream", "X-Vqd-4": retn.headers["x-vqd-4"], "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://duckduckgo.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://duckduckgo.com/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=1, i"}
    retn=requests.post(url, headers=headers,json=prompt)
    return retn.content.decode()

#question="I want 5kg potato at 2 per kg"
#_prompt = f"You are a helpful assistant and your job is to understand the Question given and extract the useful info in json format \n Question:-{question}"

question="Make a five days travel plan to switzerland"
_prompt = f"You are a helpful assistant and your job is to understand the Question given and answer it \n Question:-{question}"

prompt={"messages": [{"content": _prompt, "role": "user"}], "model": "meta-llama/Llama-3-70b-chat-hf"}
print("".join(re.findall("\"message\":\"(.+?)\",\"created\":\d+,\"id\":",queryDuck(prompt))))
