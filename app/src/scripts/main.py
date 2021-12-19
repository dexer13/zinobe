import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(parent_dir)
