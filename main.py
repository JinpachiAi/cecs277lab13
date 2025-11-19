from tasklist import TaskList
from check_input import get_int_range

"""
    LAB 13: Iterators
    Lesley Burgueno Beas
    Douglas Sam
    November 18th, 2025
    Creates a program that maintains a task list for the user.
"""

def main_menu():
    """
    Displays menu for the user. Asks user for a choice 1-6 and returns that choice
    :return:
        choice (int) : returns an int 1-6 depending on user input
    """

    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and Exit")

    choice = get_int_range("Enter your choice (1-6): ",1,6)

    return choice

def get_date():
    """
    Prompts user for month, day, year. Formats input and returns formatted date

    :return:
        formatted date (str) : returns a formatted string of the date
    """

    month = get_int_range("Enter month (1-12): ", 1, 12)
    day = get_int_range("Enter day (1-31): ", 1, 31)
    year = get_int_range("Enter year (2000-2100): ", 2000, 2100)

    formatted_month = f"{month:02d}"
    formatted_day = f"{day:02d}"
    formatted_year = str(year)

    return f"{formatted_month}/{formatted_day}/{formatted_year}"

def get_time():
    """
    Prompts user for Military time. Formats input and returns formatted time

    :return:
        formatted time (str) : returns a formatted string of the time
    """

    print("Enter time details (Military Time): ")
    hour = get_int_range("Enter hour (0-23): ", 0, 23)
    minute = get_int_range("Enter minute (0-59): ",0,59)

    formatted_hour = f"{hour:02d}"
    formatted_minute = f"{minute:02d}"

    return f"{formatted_hour}:{formatted_minute}"


def main():

    task_manager = TaskList()

    while True:
        print(f"\nTasks to complete: {len(task_manager)}")
        choice = main_menu()

        # gets current task and prints
        if choice == 1:
            current_task = task_manager.get_current_task()
            if current_task:
                print(f"Current task: {current_task}")
            else:
                print("No current tasks")

        # displays all tasks
        elif choice == 2:
            if not task_manager:
                print("No tasks to display")
            else:
                for i,task in enumerate(task_manager):
                    print(f"{i+1}. {task}")

        # sets current task to completed and displays next task
        elif choice == 3:
            completed_task = task_manager.mark_complete()
            current_task = task_manager.get_current_task()

            if completed_task:
                print(f"Marking current task as complete: {completed_task}")
                print(f"New current task is: {current_task}")
            else:
                print("Nothing to complete")

        # adds task to list
        elif choice == 4:
            desc = input("Enter task description: ")
            print("Enter a due date: ")
            date = get_date()
            time = get_time()

            task_manager.add_task(desc, date, time)

        # searches task list via date
        elif choice == 5:

            print("Enter date to search: ")
            search_date = get_date()
            found_tasks = False

            print(f"\nTasks due on {search_date}: ")

            for task in task_manager:
                if task.date == search_date:
                    print(f"- {task}")
                    found_tasks = True

            if not found_tasks:
                print(f"No tasks found matching the date {search_date}")

        # saves task list and exits
        elif choice == 6:
            task_manager.save_file()
            print("Saving List...")
            exit()



if __name__ == "__main__":
    main()