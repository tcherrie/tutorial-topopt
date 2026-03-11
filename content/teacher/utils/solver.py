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


from ngsolve import CF, cos, sin, pi
from ngsolve.webgui import Draw

def DrawMaterial(rho, theta, scene = None):
    """ plot the fibers along the parallel direction """
    mesh = rho.space.mesh
    if scene is None :
        scene = Draw(rho*CF((cos(theta+pi/2),sin(theta+pi/2))), mesh, vectors = { "grid_size":20}, 
                     settings = {"Objects" : { "Wireframe" : False } } , min=0, max=1)
        return scene
    else:
        scene.Redraw(rho*CF((cos(theta+pi/2),sin(theta+pi/2))), mesh, vectors = { "grid_size":20},
                     settings = {"Objects" : { "Wireframe" : False } }, min=0, max=1)