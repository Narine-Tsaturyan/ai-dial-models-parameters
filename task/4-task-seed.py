from task.app.main import run

# Try it with a seed
print("\nWith seed = 42")
run(
    deployment_name="gpt-4o",
    seed=42,
    n=5,
    print_only_content=False
)

# Try it without a seed for comparison
print("\nWithout seed")
run(
    deployment_name="gpt-4o",
    messages=[{"role": "user", "content": "Name a random animal"}],
    n=5,
    print_only_content=False
)