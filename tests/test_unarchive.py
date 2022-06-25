from archive_tool import *
from pathlib import Path

def test_unarchive():
    root_path = Path('./tests/test_unarchive/Lab01-中文.zip')
    print(str(root_path))
    tool = UnarchiveTool()
    tool.handle_zip(root_path)
