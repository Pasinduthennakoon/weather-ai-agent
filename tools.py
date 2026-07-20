from langchain_community.tools import DuckDuckGoSearchRun, OpenWeatherMapQueryRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()
weather_api_wrapper = OpenWeatherMapAPIWrapper()

weather_tool = OpenWeatherMapQueryRun(
    api_wrapper=weather_api_wrapper
)
