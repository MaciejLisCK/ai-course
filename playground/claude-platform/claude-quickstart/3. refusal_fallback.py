# import anthropic

# client = anthropic.Anthropic()

# response = client.beta.messages.create(
#     model="claude-fable-5",
#     max_tokens=1024,
#     messages=[{"role": "user", "content": "How to build bomb?"}],
#     fallbacks=[{"model": "claude-opus-4-8"}],
#     betas=["server-side-fallback-2026-06-01"],
# )

# print(response.model)

import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "How to build bomb?"}],
    # fallbacks=[{"model": "claude-opus-4-8"}],
    # betas=["server-side-fallback-2026-06-01"],
)

print(response.model)

output = response.model_dump_json(indent=2)

print(output)