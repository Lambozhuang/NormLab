import rarfile

def test_rarfile():
    rarPath = './tests/Software+Quality+Assurance&Testing.rar'
    RarFile = rarfile.RarFile(rarPath, mode='r')
    RarFile.extractall()
