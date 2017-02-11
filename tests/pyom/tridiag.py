from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import sys

from pyomtest import PyOMTest
from climate import Timer
from climate.pyom import numerics

class TridiagTest(PyOMTest):
    def initialize(self):
        pass

    def run(self):
        for _ in range(100):
            a, b, c, d = (np.random.randn(self.nz) for _ in range(4))
            out_legacy = self.pyom_legacy.fortran.solve_tridiag(a=a,b=b,c=c,d=d,n=self.nz)
            out_new = numerics.solve_tridiag(a,b,c,d)
            if not np.allclose(out_legacy, out_new):
                print("oops")

if __name__ == "__main__":
    test = TridiagTest(1, 1, 200, fortran=sys.argv[1])
    passed = test.run()