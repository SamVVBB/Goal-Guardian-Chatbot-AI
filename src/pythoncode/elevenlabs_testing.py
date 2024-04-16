# import elevenlabs

# audio = elevenlabs.G


# audio = elevenlabs.generate(
#     text = "Hello? is this fucking working?",
#     voice = "oOpg03UbqCoLifv3fFdV"
# )

# client.play(audio)

from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="3a34ae322ba1eee49048a66799dca5fb", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text="I've successfully added 'mow the lawn' to your to-do list.",
    voice=Voice(
        voice_id= 'ThT5KcBeYPX3keUQqHPh',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)
