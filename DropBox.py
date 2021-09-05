import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AyrvaOMGGOBByylyPsezYhr7Y9qg0gxjDxqvbNBtAgEqlCSMtlQY1jX83OzCcofTBmm5qHw7ayO-Y2MoNiIw2xTRE4MWLnBl2WBG7vVfi3cK1uERaTulpC4MF1umpj660IxSwW1r0U4'
    transferData = TransferData(access_token)

    file_from = 'xyz/mp.txt'
    file_to = '/abc/mpx.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

