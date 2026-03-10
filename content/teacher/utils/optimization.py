from ngsolve import GridFunction, LinearForm
from ngsolve.la import BaseMatrix

def solve_adjoint(state : GridFunction,     # state solution
                  rho : GridFunction,       # density
                  Kinv : BaseMatrix,        # decomposition of the state matrix
                  df : callable             # directional derivative of f, with signature df(state, rho, v) where v is the test function
                  ) -> GridFunction:
    """ Solve the linear system associated to the given bilinear and linear forms."""
    fes = state.space
    v = fes.TestFunction()
    f = LinearForm(df(state, rho, v)).Assemble().vec
    adjoint = GridFunction(fes)
    adjoint.vec.data = -1 * Kinv.T * f
    return adjoint

