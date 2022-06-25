import rarfile

def test_rarfile():
    rarPath = './tests/Software+Quality+Assurance&Testing.rar'
    RarFile = rarfile.RarFile(rarPath, mode='r')
    i = RarFile.infolist
    RarFile.extractall()

