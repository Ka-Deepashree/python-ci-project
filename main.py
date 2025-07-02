import os

TODO_FILE = "todo.txt"
print("CI Pipeline Success")
print("This is the positive build case")
print("This line will cause a syntax error)
add_task("Missing parenthesis"
raise Exception("Simulating build failure!")

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    print("Welcome to the CI/CD Pipeline Demo!")
    add_task("Prepare CI demo")
    add_task("Push code to GitHub")
    add_task("Test GitHub webhook trigger")
    list_tasks()
#webhook trigger retesting
if __name__ == "__main__":
    main()
