from task import Task

class TaskList:
    def __init__(self):
        self._tasklist = []

        try:
            with open('tasklist.txt', 'r') as file:
                for line in file:
                    try:
                        desc, date, time = line.strip().split(',')
                        new_task = Task(desc, date, time)
                        self._tasklist.append(new_task)
                    except ValueError:
                        print(f"Skipping malformed line in file: {line.strip()}")
        except FileNotFoundError:
            print(f"Starting with an empty task list, 'tasklist.txt' not found")

    def add_task(self, desc, date, time):
        new_task = Task(desc, date, time)

        self._tasklist.append(new_task)

    def get_current_task(self):

        return self._tasklist[0]

    def mark_complete(self):

        if not self._tasklist:
            return None
        return self._tasklist.pop(0)

    def save_file(self):

        with open('tasklist.txt', 'w') as file:
            for task in self._tasklist:
                file.write(repr(task) + '\n')

    def __len__(self):

        return len(self._tasklist)

    def __iter__(self):

        self._n = 0

        return self

    def __next__(self):

        if self._n >= len(self._tasklist):
            raise StopIteration

        task = self._tasklist[self._n]
        self._n += 1

        return task