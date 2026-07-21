from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, weather_tool
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0
)

class WeatherResponse(BaseModel):
    temperature: float
    weather_condition: str
    humidity: int
    wind_speed: float

prompt = """
You are a weather assistant.

When the user mentions a landmark instead of a city:

1. Use the search tool to identify the city and country.
2. Use the OpenWeatherMap tool with that city and country.
3. Report the temperature, weather condition, humidity, and wind speed.

Always use the weather tool for current weather information.
Do not guess current weather information.
"""


tools = [search_tool, weather_tool]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt,
    response_format=WeatherResponse
)

response = agent.invoke(
    {
        'messages':[
            {
                'role': 'user',
                'content': 'What is the current weather in new york?'
            }
        ]
    }
)
print(response['Structured_response'])
