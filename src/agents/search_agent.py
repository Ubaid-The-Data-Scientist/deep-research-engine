from agents import Agent, ModelSettings
from src.models.gemini import gemini_client
from src.tools.tavily_web_search_tool import web_search_tool



INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[web_search_tool],
    model=gemini_client,
    model_settings=ModelSettings(tool_choice="required")
)