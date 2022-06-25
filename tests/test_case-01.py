from pathlib import Path
from os import walk, path
from filter_tool import *
from archive_tool import UnarchiveTool
from norm_lab import LabController

def test_case_01():
    root_zip_path = Path('./tests/test-case-01/ZipInner/Lab01-中文.zip')
    # root_zip_path = Path('./tests/test-case-01/ZipOuter/Lab01-中文.zip')
    expected_path = Path('./tests/test-case-01/ExpectedOutput/')

    test_lab = LabController(root_zip_path)

    test_lab.execute(UnarchiveTool())
    test_lab.execute(FileFilterTool())
    test_lab.execute(StructureFilterTool())

    assert compare_path(root_zip_path.parent, expected_path)


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
