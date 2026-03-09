from netgen.geom2d import SplineGeometry


from ngsolve import GridFunction

def solve(bilinearForm, linearForm):
    K = bilinearForm.Assemble().mat
    f = linearForm.Assemble().vec
    fes = bilinearForm.space
    sol = GridFunction(fes)
    Kinv = K.Inverse(freedofs = fes.FreeDofs())
    sol.vec.data = Kinv * f
    return sol