from logging import root
from pathlib import Path
from os import walk, path
from src.filter_tool import *
from src.archive_tool import UnarchiveTool
from src.norm_lab import LabController

def test_case_01():
    root_zip_path_1 = Path('./tests/test-case-01/ZipInner/Lab01-中文.zip')
    root_zip_path_2 = Path('./tests/test-case-01/ZipOuter/Lab01-中文.zip')
    expected_path = Path('./tests/test-case-01/ExpectedOutput/Lab01-中文')

    test_controller_1 = LabController('test_lab', root_zip_path_1, root_zip_path_1.parent, 'test', 'test', 'test')

    test_controller_1.execute(UnarchiveTool())
    test_controller_1.execute(FileFilterTool())
    test_controller_1.execute(StructureFilterTool())

    test_controller_2 = LabController('test_lab', root_zip_path_2, root_zip_path_2.parent, 'test', 'test', 'test')

    test_controller_2.execute(UnarchiveTool())
    test_controller_2.execute(FileFilterTool())
    test_controller_2.execute(StructureFilterTool())

    assert compare_path(root_zip_path_1.parent / root_zip_path_1.stem, expected_path)
    assert compare_path(root_zip_path_2.parent / root_zip_path_2.stem, expected_path)


def compare_path(output: Path, expected: Path):
    expected_list = []
    output_list = []
    for r, ds, fs in walk(expected):
        for f in fs:
            expected_list.append(path.join(r, f)[len(str(expected)):])

    for r, ds, fs in walk(output):
        for f in fs:
            output_list.append(path.join(r, f)[len(str(output)):])

    if expected_list == output_list:
        return True
    else:
        return False            
