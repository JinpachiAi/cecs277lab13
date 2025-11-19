from task import Task

class TaskList:
    """
    Attributes:
        _tasklist : a list of Task objects
        _n : a counter for the iterator
    """
    def __init__(self):
        """
        initializes tasklist. Creates tasklist.txt if it doesn't exist. reads lists of tasks from tasklist.txt into
        tasklist list

        Raises:
            FileExistsError: file already created
            FileNoteFoundError: file directory not found
            ValueError: line incorrectly formatted and can't be added to list

        """

        self._tasklist = []

        try:
            with open('tasklist.txt', 'x') as file:
                print(f"Created a new empty file: 'tasklist.txt' ")
        except FileExistsError:
            pass
        except FileNotFoundError:
            print(f"Cannot create file")

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

        self._tasklist.sort()

    def add_task(self, desc, date, time):
        """
        Adds a task to the list, then sorts it.
        Args:
            desc (str) : description of task
            date (str) : due date of task
            time (str) : due time of task

        """
        new_task = Task(desc, date, time)

        self._tasklist.append(new_task)
        self._tasklist.sort()

    def get_current_task(self):
        """
        returns the first task in the list
        Returns:
            returns the first task in the list, or None if there is no tasklist
        """

        if not self._tasklist:
            return None
        return self._tasklist[0]

    def mark_complete(self):
        """
        pops the first task in the list, or None if there is no tasklist
        Returns:
            returns the first task in the list and pops that value
        """

        if not self._tasklist:
            return None
        return self._tasklist.pop(0)

    def save_file(self):
        """
        writes the tasklist into tasklist.txt and saves the file
        :return:
        """

        with open('tasklist.txt', 'w') as file:
            for task in self._tasklist:
                file.write(repr(task) + '\n')

    def __len__(self):
        """
        length of the tasklist when using len()
        Returns:
            returns the length of the tasklist
        """

        return len(self._tasklist)

    def __iter__(self):
        """
        initialize variable _n needed to iterate over collection
        Returns:
            the iterator object
        """

        self._n = 0

        return self

    def __next__(self):
        """
        returns next item in the sequence and adds 1 to _n
        Returns:
            returns the next item in the sequence
        Raises:
            StopIteration: signals no more items to iterate over
        """

        if self._n >= len(self._tasklist):
            raise StopIteration

        task = self._tasklist[self._n]
        self._n += 1

        return task