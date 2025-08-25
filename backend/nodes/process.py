import asyncio
import logging
import os
from typing import Any, Dict, List, Union
import dotenv

dotenv.load_dotenv()

from ..classes import InputState, ShoppingState


logger = logging.getLogger(__name__)

class Processor:
    def __init__(self):
        pass

    def process(self, shopping_state: ShoppingState) -> ShoppingState:
        print("processing")

        shoe_recommendations = self.rank_shoe_options(shopping_state)
        # Update shopping state with ranked recommendations
        shopping_state["shoe_reccomendations"] = shoe_recommendations
        
        return shopping_state
    
    def run(self, shopping_state: ShoppingState) -> ShoppingState:
        return self.process(shopping_state)
    
    def rank_shoe_options(self, shopping_state: ShoppingState) -> List[Dict[str, Any]]:
        user_size = shopping_state.get("size")
        enhanced_shoe_data = shopping_state.get("enhanced_shoe_data", {})
        
        # Separate shoes into two groups: size match and no size match
        size_match_shoes = []
        no_size_match_shoes = []
        
        for url, shoe_info in enhanced_shoe_data.items():
            # Get the sizes list from shoe_info
            available_sizes = shoe_info.get("sizes", [])
            
            # Check if user's size exists in available sizes
            if user_size in available_sizes:
                size_match_shoes.append((url, shoe_info))
            else:
                no_size_match_shoes.append((url, shoe_info))
        
        # Create ranked recommendations list: size matches first, then others
        ranked_recommendations = []
        
        # Add size matching shoes first (highest priority)
        for url, shoe_info in size_match_shoes:
            ranked_recommendations.append({
                **shoe_info,
                "url": url,
                "rank": len(ranked_recommendations) + 1,
                "size_match": True
            })
        
        # Add non-matching shoes after (lower priority)
        for url, shoe_info in no_size_match_shoes:
            ranked_recommendations.append({
                **shoe_info,
                "url": url,
                "rank": len(ranked_recommendations) + 1,
                "size_match": False
            })
        
        return ranked_recommendations