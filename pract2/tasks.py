import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_task(tasks, description, category):
    task = {'description': description, 'completed': False, 'category': category}
    tasks[len(tasks) + 1] = task

def complete_task(tasks, task_id):
    if str(task_id) in tasks:
        tasks[str(task_id)]['completed'] = True

def search_task(tasks, query):
    found_tasks = {}
    for task_id, task in tasks.items():
        if query.lower() in task['description'].lower():
            found_tasks[task_id] = task
    return found_tasks

def tasks_in_category(tasks, category):
    category_tasks = {}
    for task_id, task in tasks.items():
        if category.lower() == task['category'].lower():
            category_tasks[task_id] = task
    return category_tasks

if __name__ == '__main__':
    task_filename = 'tasks.json'
    tasks = load_tasks(task_filename)

    while True:
        print("\nТаск-трекер")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Поиск по задачам")
        print("4. Вывести все задачи в категории")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            category = input("Введите категорию задачи: ")
            add_task(tasks, description, category)
            save_tasks(task_filename, tasks)
            print("Задача добавлена.")
        elif choice == '2':
            task_id = int(input("Введите ID задачи, которую хотите отметить выполненной: "))
            complete_task(tasks, task_id)
            save_tasks(task_filename, tasks)
            print("Задача отмечена как выполненная.")
        elif choice == '3':
            query = input("Введите строку для поиска: ")
            found_tasks = search_task(tasks, query)
            if found_tasks:
                print("Найденные задачи:")
                for task_id, task in found_tasks.items():
                    print(f"ID: {task_id}, Описание: {task['description']}, Категория: {task['category']}, Выполнена: {task['completed']}")
            else:
                print("Задачи не найдены.")
        elif choice == '4':
            category = input("Введите категорию: ")
            category_tasks = tasks_in_category(tasks, category)
            if category_tasks:
                print(f"Задачи в категории '{category}':")
                for task_id, task in category_tasks.items():
                    print(f"ID: {task_id}, Описание: {task['description']}, Выполнена: {task['completed']}")
            else:
                print(f"Задачи в категории '{category}' не найдены.")
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
