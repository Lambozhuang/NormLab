from pathlib import Path

def test_path_iterdir():
    p = Path('./tests/test_path_iterdir/Lab01-中文')
    iterdir_path(p)
    
def iterdir_path(parent: Path):
    for child in parent.iterdir():
        if child.is_dir():

            # Check empty
            flag = False
            for _ in child.iterdir():
                flag = True
                break

            if flag:
                print('DIR ' + child.name, sep='\t')
                iterdir_path(child)
            else:
                print('EMPTY DIR ' + child.name, sep='\t')
        elif child.is_file():
            print('FILE ', child.name)
        else:
            print('others')

