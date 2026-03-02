from task.app.main import run

# Test the max_tokens parameter
print("\nWith max_tokens = 10")
run(
    deployment_name='gpt-4o',
    max_tokens=10,             # Set the response to max 10 tokens
    print_only_content=False    # Set to False to see the finish_reason and full response
)
