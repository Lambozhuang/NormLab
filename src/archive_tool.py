from zipfile import *
from rarfile import *
from traverse_tool import TraverseTool
from pathlib import Path

class UnArchive:
    def __init__(self) -> None:
        pass

    def extract_all(self, path: Path)  :
        self.extractall(path)

    def extract_one(self, zip_info: ZipInfo, path: Path):
        try:
            zip_info.filename = zip_info.filename.encode('cp437').decode('gbk')
        except UnicodeDecodeError:
            zip_info.filename = zip_info.filename.encode('cp437').decode('utf-8')
        except UnicodeDecodeError:
            pass
        self.extract(zip_info, path)
    
class CustomZipFile(UnArchive, ZipFile):
    def __init__(self, file: Path) -> None:
        UnArchive.__init__(self)
        ZipFile.__init__(self, file, 'r')

class CustomRarFile(UnArchive, RarFile):
    def __init__(self, file: Path) -> None:
        UnArchive.__init__(self)
        RarFile.__init__(self, file)

class UnarchiveTraverseTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()

    def handle_zip(self, file: Path, path: Path = None):
        if path == None:
            path = file.parent / file.stem

        zipfile = CustomZipFile(file)
        for zip_info in zipfile.infolist():
            zipfile.extract_one(zip_info, path)
        zipfile.close()
        file.unlink()
        self.traverse_path(path)
        
    def hendle_rar(self, file: Path):
        pass
        # print('myTool1-rar ' + str(file))

    def handle_other(self, file: Path):
        print('myTool1-other ' + str(file))
