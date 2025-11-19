

class Task:
    def __init__(self, desc, date, time):
        """
        initialized description, date, and time
        Args:
            desc (str) : a string description of the task
            date (str) : a string of date format MM/DD/YYYY
            time (str) : a string of military time format HH:MM
        """
        self._desc = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        """
        getter for date
        Returns:
            self._date : the date of the task
        """
        return self._date

    @property
    def desc(self):
        """
        getter for the description
        Returns:
            self._desc : the description of the task
        """
        return self._desc

    @property
    def time(self):
        """
        getter for the time
        Returns:
            self._time : the time of the task
        """
        return self._time

    def __str__(self):
        """
        returns a string used to display the task's information to the user
        :return:
            a formatted string of the description and due date/time
        """
        return self._desc + " - Due: " + self._date + " at " + self._time

    def __repr__(self):
        """
        returns a string used to write the task to the file
        :return:
            a formatted string of "desc,date,time"
        """
        return f"{self._desc},{self._date},{self._time}"

    def __lt__(self, other):
        """
        returns true if the self task is less than the other task. Compare by year, then month, then day, then hour, then minute,
        and then the task description by alphabetical order
        Args:
            other (object) : another task object to compare against
        Returns:
            True if self task is less than the other task.
        """

        def format_date_for_sort(date_str):
            try:
                m, d, y = date_str.split('/')
                return f"{y}/{m}/{d}"
            except ValueError:
                return date_str


        self_sort_key = (format_date_for_sort(self.date), self._time, self._desc)
        other_sort_key = (format_date_for_sort(other.date), other.time, other.desc)

        return self_sort_key < other_sort_key
