import ast
CUSTOM_FUNCTIONS = {
    "age_group": lambda age: "young" if age < 30 else "middle-aged" if age < 50 else "senior"
}

class Node:
    def __init__(self, node_type: str, left=None, right=None, value=None):
        self.type = node_type 
        self.left = left
        self.right = right
        self.value = value  

def create_rule(rule_string: str) -> Node:
    try:
        parsed_expr = ast.parse(rule_string, mode='eval')
        return _build_ast_from_expr(parsed_expr.body)
    except Exception as e:
        raise ValueError(f"Invalid rule format: {str(e)}")
def _build_ast_from_expr(expr):
    if isinstance(expr, ast.BoolOp):  
        op = 'and' if isinstance(expr.op, ast.And) else 'or'
        return Node(node_type="operator", left=_build_ast_from_expr(expr.values[0]), 
                    right=_build_ast_from_expr(expr.values[1]), value=op)
    elif isinstance(expr, ast.Compare):  
        left = _build_ast_from_expr(expr.left)
        op = _get_operator(expr.ops[0])
        right = _build_ast_from_expr(expr.comparators[0])
        return Node(node_type="operand", left=left, right=right, value=op)
    elif isinstance(expr, ast.Call):  
        func_name = expr.func.id
        arg = _build_ast_from_expr(expr.args[0])
        return Node(node_type="function_call", value=func_name, left=arg)
    elif isinstance(expr, ast.Name):  
        return Node(node_type="variable", value=expr.id)
    elif isinstance(expr, ast.Constant):
        return Node(node_type="constant", value=expr.value)
    else:
        raise ValueError("Unsupported expression format")

def _get_operator(op):
    if isinstance(op, ast.Gt):
        return ">"
    elif isinstance(op, ast.Lt):
        return "<"
    elif isinstance(op, ast.Eq):
        return "=="
    else:
        raise ValueError("Unsupported operator")
def combine_rules(rule_nodes: list[Node], operator="and") -> Node:
    if not rule_nodes:
        raise ValueError("No rules to combine")
    
    combined_ast = rule_nodes[0]
    for rule in rule_nodes[1:]:
        combined_ast = Node(node_type="operator", left=combined_ast, right=rule, value=operator)
    
    return combined_ast
def evaluate_rule(ast_node: Node, data: dict) -> bool:
    if ast_node.type == "operand":
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)
        return _evaluate_condition(left_result, ast_node.value, right_result)

    elif ast_node.type == "operator":
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)
        if ast_node.value == "and":
            return left_result and right_result
        elif ast_node.value == "or":
            return left_result or right_result
        else:
            raise ValueError(f"Unknown operator: {ast_node.value}")

    elif ast_node.type == "function_call":
        function_name = ast_node.value
        if function_name in CUSTOM_FUNCTIONS:
            arg_value = evaluate_rule(ast_node.left, data)
            return CUSTOM_FUNCTIONS[function_name](arg_value)
        else:
            raise ValueError(f"Function '{function_name}' not found in function registry")

    elif ast_node.type == "variable":
        
        return data.get(ast_node.value, None)

    elif ast_node.type == "constant":
        
        return ast_node.value

    else:
        raise ValueError("Invalid AST Node")
def _evaluate_condition(left_value, operator, right_value):
    if operator == ">":
        return left_value > right_value
    elif operator == "<":
        return left_value < right_value
    elif operator == "==":
        return left_value == right_value
    else:
        raise ValueError(f"Unsupported operator: {operator}")

