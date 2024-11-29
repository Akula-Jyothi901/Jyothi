from behave import *
from calculator import Calculator

@Given('the calculator is clear')
def step_impl(context):
    context.calculator = Calculator()
    print("calculator initialized")

@When('enter {a} and {b} and press add')
def step_impl(context, a, b):
    context.result = context.calculator.add(int(a),int(b))
    print(f"adding {a} and {b}, result: {int(context.result)}")

@Then('the result should be {expected_result}')
def step_impl(context, expected_result):
    assert context.result == expected_result, f"Expected {type(expected_result)} and got {context.result}"

@When('enter {a} and {b} and press subtract')
def step_impl(context, a, b):
    context.result = context.calculator.subtract(a,b)