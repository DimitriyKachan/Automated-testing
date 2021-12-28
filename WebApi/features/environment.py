from behave import fixture
from main import DRBOX

@fixture
def before_all(context):
    context.dbx = DRBOX("jDoTGWe41tkAAAAAAAAAATWqAbof201De4JPxNDczuVnl0-huGifwlqUjiFaw3h7")
    context.db_path = '/test_dropbox/my-file.txt'
    context.local_path = 'my-file.txt'