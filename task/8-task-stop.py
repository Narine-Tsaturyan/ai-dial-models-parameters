from task.app.main import run

# Try with a single stop string
print("\n--- stop = '\\n\\n' ---")
run(
    deployment_name='gpt-4o',
    stop="\n\n",
    print_only_content=True,
)

# Try with a list of stop triggers
print("\n--- stop = [**Embedding Layer**, **Transformer Blocks**, **Training**] ---")
run(
    deployment_name='gpt-4o',
    messages=[{"role": "user", "content": "Explain the key components of a Large Language Model architecture"}],
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"],
    print_only_content=True,
)

# Optionally, set print_only_content=False to see the full response JSON and finish_reason:
print("\n--- stop = [**Embedding Layer**, **Transformer Blocks**, **Training**] (see full JSON) ---")
run(
    deployment_name='gpt-4o',
    messages=[{"role": "user", "content": "Explain the key components of a Large Language Model architecture"}],
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"],
    print_only_content=False,
)
