import asyncio
import logging
import os
from typing import Any, Dict, List, Union
from tavily import TavilyClient
import dotenv
from ..classes import ShoppingState
from openai import OpenAI

openai_client = OpenAI()
dotenv.load_dotenv()
logger = logging.getLogger(__name__)

# should extract all the shoes from the urls
# should return a dictionary of shoe data 
# {shoe_type: x, size: y, color: z, price: a}
# then processor will use an LLM to determine the best shoe based on input data


class Extractor:

    def __init__(self) -> None:
        self.tavily_client = TavilyClient()
    
    def extract(self, state: ShoppingState) -> ShoppingState:
        print("extracting")

        enhanced_shoe_data = {}
        enhanced_shoe_data = self.extract_shoe_data(state)

        print("extraction complete")

        state["enhanced_shoe_data"] = enhanced_shoe_data
        return state

    def run(self, state: ShoppingState):
        print("running extract")
        return self.extract(state)

    def extract_from_url(self, url: str) -> str:
        response = self.tavily_client.extract(urls=url)
        return response
    
    def extract_shoe_data(self, state: ShoppingState) -> Dict[str, Any]:
        pass

        # dont try to use tavily extract right now 
        # use raw content from each shoe data and pass it to an LLM to extract the shoe data
    


def parse_raw_content_with_llm(raw_content: str) -> Dict[str, Any]:
   
   prompt = f"""
        You are a Nike product data extraction expert. Analyze the raw HTML content from a Nike product page and extract all relevant shoe information into a structured JSON format.

        Extract as many of these fields as possible from the content:

        REQUIRED FIELDS:
        - name: Full product name (e.g., "Nike Air Force 1 '07")
        - category: Product category (e.g., "Men's Shoes", "Women's Trail Running Shoes")
        - price: Current price as string (e.g., "$170", "$99.97", "See Price in Bag")

        OPTIONAL FIELDS (extract if available):
        - product_code: Nike style code (e.g., "FV3929-001", "DD1525-100") 
        - colors: Array of color combinations (e.g., ["Black/White/Cool Grey", "Summit White/Magic Ember"])
        - sizes: Array of available sizes (e.g., ["M 4 / W 5.5", "M 8.5 / W 10"])
        - description: Brief product description or key features
        - availability: Stock status if mentioned (e.g., "In Stock", "Out of Stock")


        INSTRUCTIONS:
        1. Return ONLY valid JSON - no additional text or explanations
        2. Use null for missing fields rather than empty strings
        3. For arrays, return empty array [] if no data found
        4. Extract exact text as it appears on the page
        5. If multiple prices exist, prioritize the main product price
        6. For colors, include full color descriptions as shown
        7. For sizes, maintain Nike's format (e.g., "M 8 / W 9.5")

        RAW CONTENT:
        {raw_content[:8000]}...

        Return the extracted data as JSON:
        """

   response = openai_client.responses.create(
       model="gpt-4.1",
       input=prompt
   )
   
   return response.output_text  
    
