import sys
#append the path to Polymorphic Blocks
sys.path.append('.../AutomatedProductDevelopment/PolymorphicBlocks')

import inspect

from edg import *
from products_model.ProductBlock import *
from products_model.ForcePorts import *
from products_model.PassivePort import *
import types

def elaborate_new_class(cls, superclass, filename):
    attrs = []
    attrs.append(f'    def __init__(self):\n        super().__init__()\n        self.con = self.Port(PassiveMech())')
    attrs.append(f'    def contents(self):\n        super().contents()')
    attr_string = '\n'.join(attrs)
    code = f'class {cls}({superclass}):\n{attr_string}'
    with open(filename, 'w') as f:
        f.write("from edg import *\n" + code + "\n\n")
    return code

def make_final_board(components, connections, details, finalGenCode):
    attrs = []
    deets = []
    attrs.append(f'    def contents(self):\n        super().contents()')
    for i in components:
        if i in details.keys():
            deetString = ""
            for key, value in details[i].items():
                if value != None:
                    deets.append(str(key) + " = " + "(" + str(value) + ")")
            if len(deets) > 1:
                deetString = ','.join(deets)
            elif len(deets) > 0:
                deetString = deets[0]
            attrs.append(f'        self.{i} = self.Block({i}({deetString}))')
        else:
            attrs.append(f'        self.{i} = self.Block({i}())')
    for i in connections:
        attrs.append(f'        self.connect(self.{i[0]}, self.{i[1]})')
    attr_string = '\n'.join(attrs)
    code = f'class finalboard(SimpleBoardTop):\n{attr_string}'

    with open(finalGenCode, 'w') as f:
        f.write("#Generated Code" + "\n\n")
        f.write("from edg import *\nfrom products_model.generated_code import *" + "\n\n")
        f.write(code + "\n\n")
    return code






if __name__ == "__main__":
    classes = makeclasses(Mechanical_Components, Electrical_Components, Connections)

    with open(filename, 'w') as f:
        f.write("#Generated Code" + "\n\n")
        f.write("from edg import *\nfrom products_model.ProductBlock import *\nfrom products_model.ForcePorts import *" + "\n\n")

    for name, obj in classes.items():
        code = elaborate_class(obj)
        print(code)
