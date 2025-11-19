

class Task:
    def __init__(self, desc, date, time):
        self._desc = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        return self._date

    @property
    def desc(self):
        return self._desc

    @property
    def time(self):
        return self._time

    def __str__(self):
        """
        returns a string used to display the task's information to the user
        :return:
        """
        return self._desc + " - Due: " + self._date + " at " + self._time

    def __repr__(self):
        """
        returns a string used to write the task to the file
        :return:
        """
        return f"{self._desc},{self._date},{self._time}"

    def __lt__(self, other):
        """
        returns true if the self task is less than the other task. Compare by year, then month, then day, then hour, then minute,
        and then the task description by alphabetical order
        :param other:
        :return:
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
