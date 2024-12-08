from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
 
def agent(user_id, thread_id, channel_name, message_text):
    try:
        llm = ChatNVIDIA(
            model="meta/llama-3.1-405b-instruct",
            temperature=0.1,
            top_p=1,
            max_tokens=2000,
        )
    except Exception as e:
        print(e)
        return "Error: " + str(e)
