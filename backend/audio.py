from elevenlabs import play, save
from elevenlabs.client import ElevenLabs, VoiceSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

# Access the variables
key=os.environ.get('ELEVEN_API_KEY')
client = ElevenLabs(api_key=key)

async def generate_audio(generated_response_story):
    audio = client.generate(
      text=generated_response_story,
      voice="Roger",
      model="eleven_multilingual_v2",
    )

    # Save the audio to a temporary file
    temp_file=save(audio, filename="audio3.mp3")

    return "temp_file"

#print(generate_audio("السلام عليكم"))