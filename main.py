# constraint_learner/main.py

from learner import numeric_constraints, boolean_valiant, soft_constraints, ilp_rules
from pyDatalog import pyDatalog

if __name__ == "__main__":
    print("\n🧠 Constraint Learner - Select Module:")
    print("1. Numeric Constraints (Spreadsheet)")
    print("2. Boolean Constraints (Valiant-style)")
    print("3. Soft Constraints (Fuzzy)")
    print("4. ILP Rules (Relational Logic)")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        numeric_constraints.run()
    elif choice == "2":
        boolean_valiant.run()
    elif choice == "3":
        soft_constraints.run()
    elif choice == "4":
        ilp_rules.run()
    else:
        print("Invalid choice")
