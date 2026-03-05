import os
import requests
from langchain_tavily import TavilySearch

class FoursquarePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.foursquare.com/v3/places/search"
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

    def _format_results(self, results: dict) -> str:
        """Helper to format Foursquare JSON response into a readable string."""
        if not results.get("results"):
            return "No results found."
        
        formatted_list = []
        for place in results["results"]:
            name = place.get("name", "Unknown")
            address = place.get("location", {}).get("formatted_address", "Address not available")
            formatted_list.append(f"{name} ({address})")
        
        return ", ".join(formatted_list)

    def _search_foursquare(self, place: str, category_ids: str = None, query: str = None) -> str:
        """Generic handler for Foursquare API calls."""
        params = {
            "near": place,
            "limit": 10,
            "fields": "name,location,categories"
        }
        if category_ids:
            params["categories"] = category_ids
        if query:
            params["query"] = query

        try:
            response = requests.get(self.base_url, params=params, headers=self.headers)
            response.raise_for_status()
            return self._format_results(response.json())
        except Exception as e:
            print(f"Error calling Foursquare API: {e}")
            return None

    def foursquare_search_attractions(self, place: str) -> str:
        """
        Searches for attractions using Foursquare Categories: 
        10000 (Arts & Entertainment), 16000 (Landmarks & Outdoors)
        """
        # IDs for Arts/Entertainment and Landmarks
        return self._search_foursquare(place, category_ids="10000,16000")
    
    def foursquare_search_restaurants(self, place: str) -> str:
        """
        Searches for restaurants using Foursquare Category:
        13000 (Dining and Drinking)
        """
        return self._search_foursquare(place, category_ids="13000")
    
    def foursquare_search_activity(self, place: str) -> str:
        """
        Searches for activities using Foursquare Category:
        18000 (Sports and Recreation) and generic query.
        """
        return self._search_foursquare(place, category_ids="18000", query="activities")

    def foursquare_search_transportation(self, place: str) -> str:
        """
        Searches for transportation using Foursquare Category:
        19000 (Travel and Transportation)
        """
        return self._search_foursquare(place, category_ids="19000")

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result