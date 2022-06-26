import sys
from pathlib import Path
from src.norm_lab import Normlab
from src.archive_tool import UnarchiveTool
from src.filter_tool import FileFilterTool, FindDocTool, StructureFilterTool


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('Wrong parameters!')
        exit()

    root_zip_path = Path(sys.argv[1])
    if root_zip_path.suffix != '.zip':
        print('This is not a zip file. Wrong parameters! Aborting...')
        exit()
    output_path = Path(sys.argv[2])
    info_path = Path(sys.argv[3])
    if info_path.suffix != '.csv':
        print('This is not a csv file. Wrong parameters! Aborting...')
        exit()

    print('Generating Normlab infomation...')
    test_normlab = Normlab(root_zip_path, output_path, info_path)
    print('Students infomation gathered, starting executioin...')
    test_normlab.execute(UnarchiveTool())
    print('Successfully unarchived labs.')
    test_normlab.execute(FileFilterTool())
    print('Successfully filtered ignored files.')
    test_normlab.execute(FindDocTool())
    print('Successfully found doc files.')
    test_normlab.execute(StructureFilterTool())
    print('Successfully reorganized file structures.')
    print('Done.')