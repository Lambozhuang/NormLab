from pathlib import Path
from filter_tool import FilterTraverseTool
from archive_tool import UnarchiveTraverseTool
from os import walk, path

def test_filter():
    # root_zip_path = Path('./tests/test-case-01/ZipInner/Lab01-中文.zip')
    # output_path = Path('./tests/test-case-01/ZipInner-Output/')

    root_zip_path = Path('./tests/test-case-01/ZipOuter/Lab01-中文.zip')
    output_path = Path('./tests/test-case-01/ZipOuter-Output/')

    expected_path = Path('./tests/test-case-01/ExpectedOutput/')

    archive_tool = UnarchiveTraverseTool()
    archive_tool.handle_zip(root_zip_path, output_path / root_zip_path.stem)

    root_path = output_path

    filter_tool = FilterTraverseTool()
    filter_tool.traverse_path(root_path) # filter ignore
    filter_tool.traverse_path(root_path) # prune tree

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
