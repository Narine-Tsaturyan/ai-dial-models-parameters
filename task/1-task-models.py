from task.app.main import run

models_to_try = [
    "gpt-4o",
    "claude-3-7-sonnet@20250219",
    "gemini-2.5-pro",
]

for model in models_to_try:
    print(f"\n--- Trying model: {model} ---\n")
    run(
        deployment_name=model,
        print_request=False,      # Set to True if you want to see the request JSON
        print_only_content=True,  # Set to True to print only the model's answer
    )
