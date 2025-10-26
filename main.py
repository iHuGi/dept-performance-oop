# Import the class from the other file
from departments import DepartmentAnalyzer

# Global threshold for the warning list
PASSING_THRESHOLD = 85


def main():
    # --- DATA ---
    employees = [
        {"name": "Alice", "department": "Sales", "scores": [80, 85, 90]},
        {"name": "Bob", "department": "IT", "scores": [70, 75, 72]},
        {"name": "Charlie", "department": "Sales", "scores": [88, 92, 85]},
        {"name": "David", "department": "IT", "scores": [95, 90, 93]},
        {"name": "Eve", "department": "HR", "scores": [90, 85, 88]},
        {"name": "Frank", "department": "Sales", "scores": [75, 80, 70]},
        {"name": "Grace", "department": "Marketing", "scores": [82, 83, 84]},
        {"name": "Heidi", "department": "IT", "scores": [65, 70, 68]},
    ]

    # 1. Instantiate the class (creates the object and caches grouped scores)
    analyzer = DepartmentAnalyzer(employees)

    # -------------------- DEBUGGING & DIAGNOSTICS --------------------
    print("=" * 40)
    print("  DEBUG: INITIAL STATE & CACHE CHECK")
    print("=" * 40)
    print(f"Total Employees Loaded: {len(employees)}")
    print(f"Target Warning Threshold: {PASSING_THRESHOLD}")

    print("\nPre-Grouped Scores (Cached State - from __init__):")
    # Call the diagnostic method to view the internal state
    analyzer.print_department_cache()
    print("-" * 40)
    # -----------------------------------------------------------------

    # 2. Call the object's methods to get the final reports
    avg_scores_by_dept, highest_scores_by_dept = analyzer.get_department_stats()
    employees_to_warn = analyzer.get_warning_list(PASSING_THRESHOLD)

    # --- FINAL REPORT RESULTS ---

    print("=" * 40)
    print("  EMPLOYEE PERFORMANCE ANALYSIS REPORT")
    print("=" * 40)

    print("\nAverage Score Per Department:")
    for dept, avg in avg_scores_by_dept.items():
        print(f"  📊 {dept}: {avg:.2f}")

    print("\nHighest Score Per Department:")
    for dept, high in highest_scores_by_dept.items():
        print(f"  🏆 {dept}: {high:.2f}")

    print(f"\n--- Warning List (Individual Avg. Below {PASSING_THRESHOLD}) ---")
    if employees_to_warn:
        for employee in employees_to_warn:
            print(f"  🚨 {employee['name']} ({employee['department']}) - Avg: {employee['average_score']:.2f}")
    else:
        print("  🎉 No employees are below the threshold!")

    print("=" * 40)


# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()