# Tutorial: Topology Optimization in Electrical Engineering


## 1) Quickstart

Click on the yellow badge or scan the QR code to open the JupyterLite environment to fill and execute the Jupyter notebooks:

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://tcherrie.github.io/tutorial-topopt/lab/?path=student/A_Jupyter_cheat_sheet.ipynb)

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/7b3f0679-a863-45cb-98c3-23a607340a01" />


## 2) Local installation (not required)

Download or Git clone the repository, and install the required packages in a new Python environment (version 3.13 or later). 

For doing so, open a terminal, create and activate a dedicated Python environment, using for instance `conda` (requires the installation of [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) ): 

`conda create -n myenv python=3.13`

with `myenv` being replaced by your environment name, and activate it:

`conda activate myenv`

Then, go to the folder where the code is located:

`cd C:\path\to\the\folder`

replacing `C:\path\to\the\folder` by the path to the local folder containing this code. Then, install the required packages using 

`pip install numpy scipy matplotlib jupyter ngsolve webgui_jupyter_widgets`

After that, you should be able to open Jupyter typing

`jupyter lab`

and run the scripts located in the "student" folder on your computer.

## 3) About

- Use JupyterLite, a JupyterLab distribution that runs entirely in the browser, to provide a lightweight and portable environment for teaching numerical modeling, together with [NGSolve](https://ngsolve.org/)
- Based on the following template repository : [https://github.com/NGSolve/jupyterlite_ngsolve/tree/main](https://github.com/NGSolve/jupyterlite_ngsolve/tree/main). Thanks a lot to the developers !
- Inspired from these repositories [tutoriel_optimisation_topologique_GDR_SEEDS](tcherrie/tutoriel_optimisation_topologique_GDR_SEEDS) and [https://github.com/Authomas555/sge2025_TopOpt](Authomas555/sge2025_TopOpt) associate with the paper [[Cherrière, Gauthey, Gaydier, Hage-Hassan 2025]](https://cnrs.hal.science/hal-05185001v1)
- Developed by [T. Cherrière](https://tcherrie.github.io/), [T. Gauthey](https://www.centralesupelec.fr/chercheurs/thomas-gauthey), [M. Hage-Hassan](https://www.centralesupelec.fr/chercheurs/maya-hage-hassan) (GeePs, CentraleSupélec, France) & [N. Krenn](https://www.oeaw.ac.at/ricam/staff/nepomuk-krenn) (RICAM, ÖAW, Austria).
- Thanks to S. Gaydier (G2ELab) for contributing to previous versions

Contact : <theodore.cherriere@centralesupelec.fr>

## 4) License

Copyright (C) 2026 Théodore Cherrière (theodore.cherriere@centralesupelec.fr), Thomas Gauthey (thomas.gauthey@centralesupelec.fr), Maya Hage-Hassan (maya.hage-hassan@centralesupelec.fr), Nepomuk Krenn (nepomuk.krenn@ricam.oeaw.ac.at)


This code is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 2.1 of the License, or (at your option) any later version.

This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License and of the GNU General Public License along with this code. If not, see <http://www.gnu.org/licenses/>. Please read their terms carefully and use this copy of the code only if you accept them.
