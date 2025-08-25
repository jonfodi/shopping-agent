import logging
from tavily import TavilyClient
import dotenv

from backend.classes.state import Gender, InputState

from ..classes import ShoppingState
from typing import Any, Dict

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self):
        self.tavily_client = TavilyClient()

    def crawl(self, state: ShoppingState) -> Dict[str, Any]:
        crawl_instructions = create_crawl_instructions(state)

        # Perform crawl with Tavily
        try:
            response = self.crawl_nike_with_tavily(state, crawl_instructions)
            shoe_data = process_extraction(response)
            
        except Exception as e:
            logger.error(f"Error during crawling: {str(e)}")
            shoe_data = {}
        
        state['shoe_data'] = shoe_data
        
        return {
            'shoe_data': shoe_data
        }
    
    def crawl_nike_with_tavily(self, state: InputState, crawl_instructions: str) -> Dict[str, Any]:

        url = create_crawl_url(state.get("gender"))
        print(url)
        response = self.tavily_client.crawl(
            url=url,
            instructions=crawl_instructions,
            max_results=15,
            max_breadth=2,
            include_raw_content=True,
        )
        return response

    def run(self, state: ShoppingState) -> Dict[str, Any]:
        return self.crawl(state)

def create_crawl_instructions(state: InputState) -> str:
    instructions=f"""
    Find individual nike {state.get("shoe_type")} shoe product pages that start with '/t/' in the URL. 
    Look for specific shoe models with names, prices, and product codes like 'FD2597-602' or 'HJ5940-071'. 
    All shoes should be in the '{state.get("gender")}s' category and under size {state.get("size")}
    """
    return instructions
    
def process_extraction(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process crawl results and return a dictionary keyed by URL, following the research pattern.
    Each document contains raw content and metadata for later LLM processing.
    """
    shoe_data = {}
    
    try:
        # Get results from Tavily crawl response
        crawl_results = response.get("results", [])
        
        if not crawl_results:
            logger.warning("No crawl results found in response")
            return shoe_data
        
        logger.info(f"Processing {len(crawl_results)} crawl results")
        
        # Process each crawled page following the research pattern
        for item in crawl_results:
            url = item.get("url")
            raw_content = item.get("raw_content", "")
            
            if not url or not raw_content:
                logger.warning(f"Skipping item with missing URL or content: {url}")
                continue
            
            # Only process Nike product pages with '/t/' pattern (individual product pages)
            if "/t/" not in url:
                logger.info(f"Skipping non-product page: {url}")
                continue
            
            # Extract basic title from raw content or use URL as fallback
            title = extract_title_from_content(raw_content, url)
            
            # Store in same format as research codebase
            shoe_data[url] = {
                "title": title,
                "content": raw_content,  # Full raw content for LLM processing
                "url": url,
                "source": "crawl",  # Mark as crawled content
                "content_length": len(raw_content)  # Useful for debugging
            }
            
            logger.info(f"Processed shoe page: URL={url}, Title='{title}', Content_Length={len(raw_content)}")
    
    except Exception as e:
        logger.error(f"Error processing crawl results: {e}")
        return {}
    
    logger.info(f"Successfully processed {len(shoe_data)} shoe pages")
    return shoe_data

def extract_title_from_content(raw_content: str, url: str) -> str:
    """
    Extract shoe title from raw HTML content, similar to clean_title in research codebase.
    """
    try:
        # Look for the main product title in Nike's HTML structure
        # Nike typically uses patterns like "# Nike Air Force 1 '07 Mid"
        lines = raw_content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for Nike shoe titles (usually start with # and contain Nike)
            if line.startswith('# Nike') and ('Air Force' in line or 'Air Jordan' in line or 'Air Max' in line):
                return line.replace('# ', '').strip()
            # Also look for titles in ## format
            elif line.startswith('## ') and ("Shoe" in line or "Men's" in line or "Women's" in line):
                # This is usually the category line, skip it
                continue
        
        # Fallback: try to extract from URL
        if '/t/' in url:
            # Extract shoe name from URL pattern like /t/air-force-1-07-mid-shoe-FJgWFP/
            url_parts = url.split('/t/')
            if len(url_parts) > 1:
                shoe_part = url_parts[1].split('/')[0]
                # Convert kebab-case to title case
                title = ' '.join(word.capitalize() for word in shoe_part.split('-'))
                return f"Nike {title}"
        
        return "Nike Shoe"  # Ultimate fallback
    
    except Exception as e:
        logger.warning(f"Error extracting title from content: {e}")
        return "Nike Shoe"
    

def create_crawl_url(gender: Gender) -> str:
    return f"https://www.nike.com/{gender.value}"