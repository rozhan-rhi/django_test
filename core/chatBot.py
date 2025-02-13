from .config import env_setting
import logging
from typing import Optional
from openai import AsyncOpenAI
from openai.types.beta.threads.run import Run
logger = logging.getLogger(__name__)
from pydantic import BaseModel
from typing import Dict, Any

class AIResponseFormat(BaseModel):
    type: str  
    summary: str


class ChatBot:
    def __init__(self):
        self.openai_key = env_setting["OPENAI_API_KEY"]  
        self.client = AsyncOpenAI(api_key=self.openai_key)  

    async def summerize(self, user_text: str) -> Optional[str]:
        """Send a message to OpenAI GPT and get a response."""
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4",  
                messages=[
                    {"role": "system", "content": "summerize any input text"},
                    {"role": "user", "content": f"summerize the following text in one sentence:\n\n{user_text}"}
                ],
                max_tokens=500,
                timeout=30
            )
            ai_summary = response.choices[0].message.content.strip()
            # Structure the AI response using Pydantic
            ai_response = AIResponseFormat(
                type="json_schema",
                summary=ai_summary
            )
            return ai_response.dict() 
        except Exception as e:
            logger.error(f"ChatBot Error: {e}")
            raise Exception(f"An error occurred: {e}")
