from task.app.main import run

temperatures = [0.0, 0.2, 0.5, 0.7, 1.0, 2.1]  # 2.1 to observe error/behavior

for temp in temperatures:
    print(f"\n--- Temperature: {temp} ---")
    run(
        deployment_name='gpt-4o',
        temperature=temp,
        print_only_content=True,
    )
