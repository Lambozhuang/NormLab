from traverse_tool import TraverseTool
from pathlib import Path

class Test_MyTraverseTool1(TraverseTool):
    
    def handle_zip(self, file: Path):
        print('myTool1-zip ' + str(file))
        
    def hendle_rar(self, file: Path):
        print('myTool1-rar ' + str(file))

    def handle_other(self, file: Path):
        print('myTool1-other ' + str(file))

def test_traverse_tool():
    my_traverse_tool1 = Test_MyTraverseTool1()
    p = Path('./tests/test_path/Lab01-中文')
    my_traverse_tool1.traverse_path(p)