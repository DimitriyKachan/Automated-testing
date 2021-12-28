from behave import fixture
from main import DRBOX

@fixture
def before_all(context):
    context.dbx = DRBOX("jDoTGWe41tkAAAAAAAAAATWqAbof201De4JPxNDczuVnl0-huGifwlqUjiFaw3h7")
    context.db_path = '/test_dropbox/my-file.txt'
    context.local_path = 'my-file.txt'
    context.hash = "6680bbec0d05d3eaac9c8b658c40f28d2f0cb0f245c7b1cabf5a61c35bd03d8e"
