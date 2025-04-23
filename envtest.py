from dotenv import load_dotenv
load_dotenv()

import os
print("OPENAI:", os.getenv("OPENAI_API_KEY"))
print("LEONARDO:", os.getenv("LEONARDO_API_KEY"))
