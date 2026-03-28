from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class Answer(BaseModel):
    steps: str = Field(description="Solution steps")
    final_answer: int = Field(description="Final numeric answer")

def initialize_chat_model(model_name, api_key, temperature=0):
    return ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        openai_api_key=api_key
    ).bind_tools([Answer])
