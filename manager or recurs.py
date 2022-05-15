class ManagerContext:
    def __enter__(self):
        print("Выполнено __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выполнено __exit__")

with ManagerContext():
    print("Between")



