from task.app.main import run

penalties = [-2.0, -1.0, 0.0, 1.0, 2.0]

for presence in penalties:
    print(f"\n--- presence_penalty = {presence} ---")
    run(
        deployment_name='gpt-4o',
        presence_penalty=presence,
        print_only_content=True
    )
