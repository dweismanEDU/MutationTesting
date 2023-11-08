import re

# Read the original source code
with open('Polynomial.py', 'r') as file:
    original_code = file.read()

# Define a list of mutation functions
def coefficient_change(code):
    # Change the first non-zero coefficient found
    return re.sub(r'(?<=\[\s*[-+]?)(\d+)', '99', code, count=1)

def arithmetic_operator_change(code):
    # Change the first '+' operator to '-' in the __add__ method
    return code.replace('a + b', 'a - b', 1)

def exponent_change(code):
    # Change the first exponentiation to a different power
    return re.sub(r'(\*\* \()(\d+)', r'\g<1>3', code, count=1)

def boundary_condition_change(code):
    # Change the epsilon value in find_root_bisection
    return code.replace('epsilon=1e-6', 'epsilon=1e-4', 1)

# Define a list of mutations to apply
mutations = [
    ('coefficient_change', coefficient_change),
    ('arithmetic_operator_change', arithmetic_operator_change),
    ('exponent_change', exponent_change),
    ('boundary_condition_change', boundary_condition_change)
]

# Apply mutations
for name, mutation_function in mutations:
    mutated_code = mutation_function(original_code)
    with open(f'polynomial_{name}.py', 'w') as mutated_file:
        mutated_file.write(mutated_code)
    print(f'Mutation {name} applied and saved to polynomial_{name}.py')
