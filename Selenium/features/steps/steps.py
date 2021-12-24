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
    context.drive.add_paygrade("Smith", "CAD - Canadian Dollar", "1500", "3000")


@then("check for existence")
def step_check(context):
    assert not context.drive.check_existence("Smith"), "Have not made"


@when("the user deletes this record")
def step_delete(context):
    context.drive.delete_row("Smith")


@then("check for absence")
def step_check_del(context):
    assert not context.drive.check_existence("Smith"), "Have not deleted"
