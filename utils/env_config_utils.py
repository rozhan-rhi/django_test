from dotenv import load_dotenv
import os

def load_env_config():
    load_dotenv(override=True)

    config = {
        "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY"),
    #    "OPENAI_ASSISTANT_ID" : os.getenv("OPENAI_ASSISTANT_ID")
    }

    return config