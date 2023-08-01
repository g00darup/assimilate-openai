import os
import openai





openai.api_key = os.environ.get("OPEN_AI_KEY")

# animal = """Suggest three names for an animal that is a superhero.
# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:"""

# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=animal,
#     temperature=0.6,
# )

# print(openai.api_key)

prompt = "Say this is a test"

response = openai.Completion.create(
    engine="text-davinci-001", prompt=prompt, max_tokens=6
)

print(response)