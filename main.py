from departments import DepartmentAnalyzer

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

    # 1. Instantiate the class
    analyzer = DepartmentAnalyzer(employees)

    # 2. Call the object's methods
    avg_scores_by_dept, highest_scores_by_dept = analyzer.get_department_stats()
    employees_to_warn = analyzer.get_warning_list(PASSING_THRESHOLD)

    # --- PRINT RESULTS ---

    print("=" * 40)
    print("  EMPLOYEE PERFORMANCE ANALYSIS (Modular)")
    print("=" * 40)

    print("\n--- Department Statistics ---")

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


# This is the standard entry point for Python scripts
if __name__ == "__main__":
    main()