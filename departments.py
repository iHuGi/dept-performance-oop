import statistics
from collections import defaultdict

class DepartmentAnalyzer:
    """
    Manages and analyzes employee data, providing departmental statistics
    and performance reports.
    """

    def __init__(self, employee_data):
        self.employees = employee_data
        self._department_scores = self._group_scores_by_department()

    def _group_scores_by_department(self):
        """Internal helper method to aggregate scores."""
        department_scores = defaultdict(list)
        for employee in self.employees:
            department_scores[employee["department"]].extend(employee["scores"])
        return department_scores

    def get_department_stats(self):
        """
        Calculates and returns the average and highest score for each department.
        Returns a tuple: (department_averages, department_highest)
        """
        department_averages = {}
        department_highest = {}

        for department, scores in self._department_scores.items():
            department_averages[department] = statistics.mean(scores)
            department_highest[department] = max(scores)

        return department_averages, department_highest

    def get_warning_list(self, threshold):
        """
        Identifies employees whose individual average score is below the given threshold.
        """
        warning_employees = []

        for employee in self.employees:
            employee_avg = statistics.mean(employee["scores"])

            if employee_avg < threshold:
                warning_employees.append({
                    "name": employee["name"],
                    "department": employee["department"],
                    "average_score": employee_avg
                })

        return warning_employees