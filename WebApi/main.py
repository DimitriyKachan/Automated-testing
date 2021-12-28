import dropbox as db


class DRBOX:
    def __init__(self, TOKEN):
        self.dbx = db.Dropbox(TOKEN)

    def upload_file(self, file_from, file_to):

        with open(file_from, 'rb') as f:
            self.dbx.files_upload(f.read(), file_to)
            print("Uploaded")

    def get_metadata(self, path1):
        return self.dbx.files_get_metadata(path=path1)

    def delete_file(self, path1):
        self.dbx.files_delete(path=path1)
        print("Deleted")

    def upload_check(self, path):
        try:
            self.dbx.files_get_metadata(path)
            return True
        except:
            return False

    def delete_check(self, path):
        try:
            self.dbx.files_get_metadata(path)
            return False
        except:
            return True

    def metadata_check(self, path):
        hash = "6680bbec0d05d3eaac9c8b658c40f28d2f0cb0f245c7b1cabf5a61c35bd03d8e"
        if self.dbx.files_get_metadata(path=path).content_hash == hash:
            return True
        else:
            return False


TOKEN = "jDoTGWe41tkAAAAAAAAAATWqAbof201De4JPxNDczuVnl0-huGifwlqUjiFaw3h7"
dbx = DRBOX(TOKEN)

file_from = 'my-file.txt'
file_path = '/test_dropbox/my-file.txt'

dbx.upload_file(file_from, file_path)
print(dbx.get_metadata(file_path).content_hash)
dbx.delete_file(file_path)
