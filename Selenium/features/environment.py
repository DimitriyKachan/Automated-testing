from behave import fixture, use_fixture
from main import Driver

@fixture
def before_all(context):
    context.drive = Driver()
    context.name = "Smith"
    context.currency = "CAD - Canadian Dollar"
    context.min = "1500"
    context.max = "3000"
