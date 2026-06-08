class Task:
    def __init__(self, id: int, description: str = "", priority: int = 1):
        self.id = id
        self.description = description
        self.priority = priority


class Queue:
    def __init__(self):
        self.items = []

    def add_task(self, task: Task):
        self.items.append(task)

    def remove_task(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def find_by_id(self, id: int):
        for task in self.items:
            if task.id == id:
                return True
        return False

    def show_tasks(self):
        print("Задачи:")
        for i in range(len(self.items)):
            ost = self.items[i]
            print(f'{i + 1}. {ost.description} (приоритет = {ost.priority}, id = {ost.id})')


if __name__ == "__main__":
    queue = Queue()

    task1 = Task(1, "Обновить зависимости проекта", 2)
    queue.add_task(task1)

    task2 = Task(2, "Написать документацию", 1)
    queue.add_task(task2)

    task3 = Task(3, "Исправить баг в авторизации", 3)
    queue.add_task(task3)

    queue.show_tasks()

    print(f'\nЕсть задача с id=2: {queue.find_by_id(2)}')
    print(f'Есть задача с id=99: {queue.find_by_id(99)}')
    print(f'\nПервая в очереди: {queue.peek().description}')
    queue.remove_task()
    print(f'После удаления первая: {queue.peek().description}')
