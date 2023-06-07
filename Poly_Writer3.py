import sys
sys.path.append('C:/Users/josep/OneDrive - Imperial College London/Year4/MastersProject/AutomatedProductDevelopment/PolymorphicBlocks')

import inspect

from edg import *
from products_model.ProductBlock import *
from products_model.ForcePorts import *
from products_model.PassivePort import *
import types

filename = 'C:/Users/josep/OneDrive - Imperial College London/Year4/MastersProject/AutomatedProductDevelopment/PolymorphicBlocks/products_model/generated_code.py'
filename2 = 'C:/Users/josep/OneDrive - Imperial College London/Year4/MastersProject/AutomatedProductDevelopment/PolymorphicBlocks/products_model/generated_final_code.py'

Mechanical_Components = ['enclosure', 'bracket']
Electrical_Components = ['amplifier', 'crossover_network', 'input_module', 'wiring', 'speaker', 'power_supply', 'audio_input', 'volume_control', 'protection_circuit']
#Connections = [['amplifier', 'speaker'], ['crossover_network', 'speaker'], ['amplifier', 'power_supply', 'speaker'], ['amplifier', 'audio_input'], ['amplifier', 'volume_control'], ['amplifier', 'protection_circuit', 'speaker']]



def makeclasses(Mechanical_Components, Electrical_Components, Connections):
    class_objects = {}
    for component in Mechanical_Components:
        print(component)
        class_objects[component] = type(component, (MechanicalBlock,), {
        })
    for component in Electrical_Components:
        class_objects[component] = type(component, (DiscreteApplication,), {})

    print(class_objects)

    for connection in Connections:
        source = class_objects[connection[0]]
        target = class_objects[connection[1]]
        setattr(source, connection[1], target)

    return class_objects


def elaborate_class(cls):
    class_name = cls.__name__
    superclasses = ', '.join(c.__name__ for c in cls.__bases__)
    attrs = []
    attrs.append(f'    def __init__(self):\n        super().__init__()\n        self.con = self.Port(PassiveMech())')
    attrs.append(f'    def contents(self):\n        super().contents()')
    attr_string = '\n'.join(attrs)
    code = f'class {class_name}({superclasses}):\n{attr_string}'
    with open(filename, 'a') as f:
        f.write(code + "\n\n")
    return code

def elaborate_final_class(components):
    firstcomp = components[0]
    secondcomp = components[1]
    attrs = []
    #attrs.append(f'    def __init__(self):\n        super().__init__()')
    attrs.append(f'    def contents(self):\n        super().contents()\n        self.comp1 = self.Block({firstcomp}())\n        self.comp2 = self.Block({secondcomp}())\n        self.connect(self.comp1.con, self.comp2.con)')
    attr_string = '\n'.join(attrs)
    code = f'class finalboard(DesignTop):\n{attr_string}'

    with open(filename2, 'w') as f:
        f.write("#Generated Code" + "\n\n")
        f.write("from edg import *\nfrom products_model.ProductBlock import *\nfrom products_model.ForcePorts import *\nfrom products_model.generated_code import *\nfrom products_model.PassivePort import *" + "\n\n")
        f.write(code + "\n\n")
    return code


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