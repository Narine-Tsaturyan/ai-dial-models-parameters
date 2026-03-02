from task.app.main import run

penalties = [-2.0, -1.0, 0.0, 1.0, 2.0]

for freq_penalty in penalties:
    print(f"\n--- frequency_penalty = {freq_penalty} ---")
    run(
        deployment_name='gpt-4o',
        frequency_penalty=freq_penalty,
        print_only_content=True
    )
