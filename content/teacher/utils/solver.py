from ngsolve import GridFunction, LinearForm, BilinearForm
from ngsolve.la import BaseMatrix

def solve(bilinearForm :LinearForm, 
          linearForm : BilinearForm
          ) -> tuple[GridFunction, BaseMatrix]:
    """ Solve the linear system associated to the given bilinear and linear forms."""
    K = bilinearForm.Assemble().mat
    f = linearForm.Assemble().vec
    fes = bilinearForm.space
    sol = GridFunction(fes)
    Kinv = K.Inverse(freedofs = fes.FreeDofs())
    sol.vec.data = Kinv * f
    return sol, Kinv