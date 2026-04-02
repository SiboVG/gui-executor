from gui_executor.exec import exec_task


@exec_task()
def print_hello(name: str = "World") -> str:
    """A simple task that prints a greeting message."""
    print(f"Hello, {name}!")
    return f"Greeted {name}."
