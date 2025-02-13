from .config import env_setting
import logging
from typing import Optional
from openai import AsyncOpenAI
from openai.types.beta.threads.run import Run
logger = logging.getLogger(__name__)


class ChatBot:
    def __init__(self):
        self.openai_key = env_setting["OPENAI_API_KEY"]  
        self.client = AsyncOpenAI(api_key=self.openai_key)  

    async def summerize(self, user_message: str) -> Optional[str]:
        """Send a message to OpenAI GPT and get a response."""
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4",  
                messages=[
                    {"role": "system", "content": "summerize any input text"},
                    {"role": "user", "content": f"summerize the following text in one sentence:\n\n{user_message}"}
                ],
                max_tokens=500,
                timeout=30
            )
            return response.choices[0].message.content.strip()  # Return AI response

        except Exception as e:
            logger.error(f"ChatBot Error: {e}")
            raise Exception(f"An error occurred: {e}")
