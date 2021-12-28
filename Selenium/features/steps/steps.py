from behave import given, when, then


@given("the user is on the login page")
def step_initialisation(context):
    pass


@when("the user logs in")
def step_log(context):
    context.drive.login("https://opensource-demo.orangehrmlive.com/")


@when("the user opens Pay Grades tab")
def step_open(context):
    context.drive.go_to_PayGrades()


@when("the user adds new record")
def step_add_new(context):
   context.drive.add_paygrade(context.name, context.currency, context.min, context.max)


@then("check for existence")
def step_check(context):
    assert not context.drive.check_existence(context.name), "Have not made"


@when("the user deletes this record")
def step_delete(context):
    context.drive.delete_row(context.name)


@then("check for absence")
def step_check_del(context):
    assert not context.drive.check_existence(context.name), "Have not deleted"
