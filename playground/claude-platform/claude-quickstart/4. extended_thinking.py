import anthropic
from anthropic.types import ThinkingConfigEnabledParam

client = anthropic.Anthropic()

thinking: ThinkingConfigEnabledParam =  {
    "type": "enabled",
    "budget_tokens": 10000,
    "display": "summarized"
}

response = client.messages.create(
    model="claude-sonnet-4-6",
    thinking=thinking,
    max_tokens=15000,
    messages=[
        {"role": "user", "content": "Ile to jest 27 * 453? Podaj sam wynik."}
    ]
)

output = response.model_dump_json(indent=2)

print(output)