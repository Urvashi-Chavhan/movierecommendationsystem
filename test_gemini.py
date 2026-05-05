from google import genai
import toml

secrets = toml.load(".streamlit/secrets.toml")
key = secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, recommend me a good movie!"
)
print(response.text)