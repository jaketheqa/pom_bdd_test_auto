from behave import given, when, then

"""
TC1 Scenario: Describe Scenario
Use same step_impl function when steps are duplicated.
"""


@given("Step1")
def step_impl(context):
    # Step 동작 구현
    print("Put the System in a Known State")


@when("Step2")
def step_impl(context):
    # Step 동작 구현
    print("Take Key Actions")


@then("Step3")
def step_impl(context):
    # Step 동작 구현
    print("Observe Outcomes.")
