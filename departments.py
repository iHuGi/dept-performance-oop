import statistics
from collections import defaultdict

class DepartmentAnalyzer:
    """
    Manages and analyzes employee data, providing departmental statistics
    and performance reports.
    """

    def __init__(self, employee_data):
        # The employee data is stored as an instance attribute (state)
        self.employees = employee_data

        # Caching the grouped scores immediately for efficiency
        self._department_scores = self._group_scores_by_department()

    # --- Internal Helper Methods ---

    def _group_scores_by_department(self):
        """Internal helper method to aggregate scores."""
        department_scores = defaultdict(list)
        for employee in self.employees:
            department_scores[employee["department"]].extend(employee["scores"])
        return department_scores

    # --- Reporting Methods ---

    def get_department_stats(self):
        """
        Calculates and returns the average and highest score for each department
        using the cached, grouped data.
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

        # This method iterates over the raw list because it's an individual assessment
        for employee in self.employees:
            employee_avg = statistics.mean(employee["scores"])

            if employee_avg < threshold:
                warning_employees.append({
                    "name": employee["name"],
                    "department": employee["department"],
                    "average_score": employee_avg
                })

        return warning_employees

    # --- Debugging Method ---

    def print_department_cache(self):
        """
        Public diagnostic method to display the internal, cached state of grouped scores.
        """
        if self._department_scores:
            for dept, scores in self._department_scores.items():
                print(f"  {dept}: {len(scores)} total scores -> {scores}")
        else:
            print("  Cache is empty.")