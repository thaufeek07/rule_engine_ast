from engine.ast_engine import create_rule, evaluate_rule, combine_rules
def main():
    rule1 = create_rule("age_group(age) == 'young' and salary > 50000")
    rule2 = create_rule("experience > 5 or department == 'Sales'")
    combined_rule = combine_rules([rule1, rule2], operator="and")
    data = {"age": 25, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_rule, data)
    print(f"Is the user eligible? {result}")
if __name__ == '__main__':
    main()
