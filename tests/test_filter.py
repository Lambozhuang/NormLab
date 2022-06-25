from pathlib import Path
from filter_tool import FilterTraverseTool
from archive_tool import UnarchiveTool

def test_filter():
    root_zip_path = Path('./tests/test_filter/Lab01-中文.zip')

    archive_tool = UnarchiveTool()
    archive_tool.handle_zip(root_zip_path)

    root_path = root_zip_path.parent / root_zip_path.stem

    filter_tool = FilterTraverseTool()
    filter_tool.traverse_path(root_path) # filter ignore
    filter_tool.traverse_path(root_path) # prune tree