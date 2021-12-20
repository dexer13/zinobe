import sys
import pathlib

parent_dir = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(parent_dir)
from app.src.core.views import CountryView


def todo():
    if CountryView().export_countries():
        print('SUCCESS')
    else:
        print('ERROR')


todo()
