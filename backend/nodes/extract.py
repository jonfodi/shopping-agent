import json
import asyncio
import logging
import os
from typing import Any, Dict, List, Union
from tavily import TavilyClient
import dotenv
from ..classes import ShoppingState
from openai import OpenAI


dotenv.load_dotenv()
logger = logging.getLogger(__name__)


class Extractor:

    def __init__(self) -> None:
        self.tavily_client = TavilyClient()
        self.openai_client = OpenAI()
    
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

        enhanced_shoe_data = {}
        shoe_data = state.get("shoe_data")
        for url, shoe_info in shoe_data.items():
            raw_content =  shoe_info.get('content', '') 
            json_shoe_data = self.parse_raw_content_with_llm(raw_content)
            enhanced_shoe_data[url] = json_shoe_data
        return enhanced_shoe_data


    def parse_raw_content_with_llm(self, raw_content: str) -> Dict[str, Any]:
    
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
    {raw_content}

    Return the extracted data as JSON:
    """

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "system", "content": "You are a precise data extraction assistant. Return only valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=1000
            )
            
            # Parse the JSON response
            response_text = response.choices[0].message.content.strip()
            
            # Remove any markdown formatting if present
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
                
            extracted_data = json.loads(response_text)
            return extracted_data
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {e}")
            return {}