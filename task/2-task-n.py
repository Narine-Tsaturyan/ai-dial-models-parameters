from task.app.main import run

models_to_try = [
    "gpt-4o",
    "claude-3-7-sonnet@20250219",
    "gemini-2.5-pro",
]

n_values = [1, 2, 3, 4, 5]

for model in models_to_try:
    for n in n_values:
        print(f"\n--- Model: {model}, n={n} ---")
        run(
            deployment_name=model,
            n=n,
            print_request=False,        # Set to True for full request info
            print_only_content=False    # Set to False to see full response with all choices
        )