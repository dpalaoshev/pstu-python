import json

def load_budget(filename):
    try:
        with open(filename, 'r') as file:
            budget_data = json.load(file)
    except FileNotFoundError:
        budget_data = {'transactions': [], 'categories': {}, 'limits': {}}
    return budget_data

def save_budget(filename, budget_data):
    with open(filename, 'w') as file:
        json.dump(budget_data, file, ensure_ascii=False, indent=4)

def add_transaction(budget_data, description, amount, category):
    transaction = {'description': description, 'amount': amount, 'category': category}
    budget_data['transactions'].append(transaction)
    if category in budget_data['categories']:
        budget_data['categories'][category] += amount
    else:
        budget_data['categories'][category] = amount

def category_analytics(budget_data, category):
    total_amount = 0
    for transaction in budget_data['transactions']:
        if transaction['category'] == category:
            total_amount += transaction['amount']
    return total_amount

def set_category_limit(budget_data, category, limit):
    budget_data['limits'][category] = limit

def check_category_limit(budget_data, category):
    if category in budget_data['limits']:
        total_amount = category_analytics(budget_data, category)
        limit = budget_data['limits'][category]
        return total_amount > limit
    return False

if __name__ == '__main__':
    budget_filename = 'budget.json'
    budget_data = load_budget(budget_filename)

    while True:
        print("\nБюджетный трекер")
        print("1. Добавить транзакцию")
        print("2. Аналитика по категориям")
        print("3. Установить лимит на категорию")
        print("4. Проверить лимит по категории")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            description = input("Введите описание операции: ")
            amount = float(input("Введите сумму: "))
            category = input("Введите категорию: ")
            add_transaction(budget_data, description, amount, category)
            save_budget(budget_filename, budget_data)
            print("Транзакция добавлена.")
        elif choice == '2':
            category = input("Введите категорию для анализа: ")
            total_amount = category_analytics(budget_data, category)
            print(f"Сумма по категории '{category}': {total_amount}")
        elif choice == '3':
            category = input("Введите категорию, для которой хотите установить лимит: ")
            limit = float(input("Введите лимит: "))
            set_category_limit(budget_data, category, limit)
            save_budget(budget_filename, budget_data)
            print(f"Лимит на категорию '{category}' установлен.")
        elif choice == '4':
            category = input("Введите категорию, для которой хотите проверить лимит: ")
            if check_category_limit(budget_data, category):
                print(f"Превышен лимит по категории '{category}'!")
            else:
                print(f"Лимит по категории '{category}' не превышен.")
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")
