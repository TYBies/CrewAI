import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html


class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    #url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    url = f"https://api.scrapingant.com/v2/general?url=https%3A%2F%2Fexample.com&x-api-key=1534f25c413a45faaf98f807a35071ba"
    
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []
    for chunk in content:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing research and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a the world greatest Research institute company and you have the world record on any research topic you now need to do research about a given topic so that you can set a new world record.",
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
    return "\n\n".join(summaries)
