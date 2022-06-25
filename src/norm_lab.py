from pathlib import Path
from zipfile import *
import csv
from pip import List
from archive_tool import CustomZipFile, UnarchiveTool
from filter_tool import *
from traverse_tool import TraverseTool

class LabController():
    def __init__(self, lab_name: str, zip_path: Path, output_path: Path, id: str, full_name: str, short_name: str) -> None:
        self.__lab_name = lab_name
        self.__path = zip_path.parent / zip_path.stem
        self.__output_path = output_path
        self.__zip_path = zip_path
        self.__id = id
        self.__full_name = full_name
        self.__short_name = short_name
        self.__doc_path_list: List[Path] = []

    def execute(self, tool: TraverseTool) -> None:
        if type(tool) == UnarchiveTool:
            tool.traverse_path(self.__zip_path)
        elif type(tool) is FindDocTool:
            name = self.__lab_name + '-' + self.__id + '-' + self.__short_name
            self.__path = self.__path.replace(self.__path.parent / name)
            tool.reset()
            tool.traverse_path(self.__path)
            self.__doc_path_list = tool.get_doc_path_list()
            count = 1
            for doc in self.__doc_path_list:
                _name = name
                if count != 1:
                    _name += '-' + str(count)
                _name += doc.suffix
                doc.replace(self.__output_path / _name)
                count += 1
        else:
            tool.traverse_path(self.__path)

    def export(self, lab_name: str, out_path: Path) -> None:
        pass

    def get_doc_path_list(self):
        return self.__doc_path_list

class Normlab():
    def __init__(self, path: Path, output_path: Path, info_path: Path) -> None:
        self.__lab_name = str(path.stem.split('-')[0])
        self.__zip_path = path
        self.__output_path = output_path
        self.__student_info_path = info_path
        self.__student_info = self.get_student_info()
        self.__controller_list: List[LabController] = []

        self.unzip_root()
        self.filter_root()
        self.generate_controllers()

    def get_student_info(self):
        with open(self.__student_info_path, encoding='utf-8-sig') as student_info:
            reader = csv.DictReader(student_info)
            info = [row for row in reader]
            return info

    def unzip_root(self) -> None:
        archive_file = CustomZipFile(self.__zip_path)
        for info in archive_file.infolist():
            archive_file.extract_one(info, self.__output_path)
        archive_file.close()
        # path.unlink()

    def filter_root(self):
        file_filter_tool = FileFilterTool()
        file_filter_tool.check_dir(self.__output_path)

    def generate_controllers(self):
        for lab in self.__output_path.iterdir():
            id = lab.stem.split('-')[0]
            full_name = self.get_full_name(id)
            short_name = self.get_short_name(id)
            # print(id)
            # print(short_name)
            new_controller = LabController(lab_name=self.__lab_name, zip_path=lab, output_path=self.__output_path, id=id, full_name=full_name, short_name=short_name)
            self.__controller_list.append(new_controller)
    
    def get_full_name(self, id: str):
        for info in self.__student_info:
            if info['StuID'] == id:
                return info['Full Name']

    def get_short_name(self, id: str):
        for info in self.__student_info:
            if info['StuID'] == id:
                return info['Short Name']

    def execute(self, tool: TraverseTool):
        for controller in self.__controller_list:
            # print(controller.get_name())
            # print(controller.get_path())
            controller.execute(tool)

    def export(self):
        for controller in self.__controller_list:
            controller.export(self.__lab_name, self.__output_path)