from pathlib import Path
from os import walk, path
from filter_tool import *
from archive_tool import *


from norm_lab import LabController, Normlab

def test_case_02():
    root_zip_path = Path('./tests/test-case-02/Lab03-JUnit for Unit Test.zip')
    output_path = Path('./tests/test-case-02/Output/Lab03-JUnit for Unit Test')
    info_path = Path('./student_info/International Student List.csv')
    expected_path = Path('./tests/test-case-02/Output-Expected/Lab03-JUnit for Unit Test')

    test_normlab = Normlab(root_zip_path, output_path, info_path)
    test_normlab.execute(UnarchiveTool())
    test_normlab.execute(FileFilterTool())
    test_normlab.execute(FindDocTool())
    test_normlab.execute(StructureFilterTool())

    assert compare_path(output_path, expected_path)


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