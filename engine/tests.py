# engine/tests.py
import unittest
from engine.ast_engine import create_rule, evaluate_rule, combine_rules

class TestRuleEngine(unittest.TestCase):
    def test_age_group_function(self):
        rule = create_rule("age_group(age) == 'young'")
        data = {"age": 25}
        result = evaluate_rule(rule, data)
        self.assertTrue(result)

    def test_combined_function_rule(self):
        rule1 = create_rule("age_group(age) == 'young'")
        rule2 = create_rule("salary > 50000")
        combined_rule = combine_rules([rule1, rule2], operator="and")
        
        data = {"age": 25, "salary": 60000}
        result = evaluate_rule(combined_rule, data)
        self.assertTrue(result)

    def test_invalid_function(self):
        # Rule with invalid function
        rule = create_rule("invalid_function(age) == 'young'")
        data = {"age": 25}
        with self.assertRaises(ValueError):
            evaluate_rule(rule, data)

if __name__ == '__main__':
    unittest.main()
