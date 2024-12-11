import sys
from autogen import AssistantAgent
from autogen import UserProxyAgent
from autogen import register_function
import tool as tl


configList = [
    {
        "model": "Qwen2.5-Coder",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
]

assistant = AssistantAgent(
    name ="assistant",
    llm_config={
        "config_list": configList,
        "temperature": 0,
    },
    system_message="""You are a web scraper that finds stock prices. You will get the stock price from a Google search. The URL format looks like this: https://www.google.com/search?client=firefox-b-d&q=apple+stock+price. Replace 'apple' with the stock name the user asks for. Provide the full URL as the search query. Once you find and show the stock price, reply with 'TERMINATE'
    """
)

user_proxy = UserProxyAgent(
    name="userproxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x:x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
)

register_function(
    tl.get_stock_price,
    caller=assistant,
    executor=user_proxy,
    name="get_stock_prices",
    description="gets the current stock price of META"
)

reply = user_proxy.initiate_chat(
    assistant,
    message="""{}""".format(sys.argv[1]),
    summary_method="last_msg"
)
