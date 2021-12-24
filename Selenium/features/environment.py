from behave import fixture, use_fixture
from main import Driver

@fixture
def before_all(context):
    context.drive = Driver()