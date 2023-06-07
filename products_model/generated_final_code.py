#Generated Code

from edg import *
from products_model.ProductBlock import *
from products_model.ForcePorts import *
from products_model.generated_code import *
from products_model.PassivePort import *

class finalboard(DesignTop):
    def contents(self):
        super().contents()
        self.comp1 = self.Block(durable_fabric())
        self.comp2 = self.Block(reinforced_handle())
        self.connect(self.comp1.con, self.comp2.con)

