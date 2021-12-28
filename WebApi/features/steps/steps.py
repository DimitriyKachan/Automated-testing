from behave import given, when, then


@given("logged in dropbox")
def step_initialisation(context):
    pass


@when("user uploads")
def step_upload(context):
    context.dbx.upload_file(context.local_path, context.db_path)


@when("the user gets metadata")
def step_get_meta(context):
    context.dbx.get_metadata(context.db_path)


@when("user deletes")
def step_add_new(context):
    context.dbx.delete_file(context.db_path)


@then("check for existence")
def step_check(context):
    assert context.dbx.upload_check(context.db_path), "Have not made"


@then("check metadata")
def step_check_meta(context):
    assert context.dbx.metadata_check(context.db_path), "Wrong file"


@then("check for absence")
def step_check_del(context):
    assert context.dbx.delete_check(context.db_path), "Have not deleted"
