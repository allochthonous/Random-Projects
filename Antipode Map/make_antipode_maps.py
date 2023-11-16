#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:35:00 2023

@author: crowan
"""

import numpy as np
import xarray as xr
from antipode_plotters import antipode_map_Robinson, antipode_map_Perspective

# load gridfile containing antipodal classifications
antipodes=xr.open_dataset('antipode_grid.nc')
antipodes.close()
# set up things correctly for plotting
# probably can do this with xarray, but don't want to rework plot formats right now
X,Y=np.meshgrid(antipodes.coords['Long'].values,antipodes.coords['Lat'].values)
result=antipodes.antipode_type.values 

# plot of just onland antipode classifications - without a reference point Perspective is less useful
fig=antipode_map_Robinson(X,Y,result, ShowPoint=False, filename="./images/Antipodal_Lithosphere_Type_No_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, ShowPoint=False, filename="./images/Antipodal_Lithosphere_Type_No_Oceans_Perspective.png")

# plot of all antipode classifications - without a reference point persepctive is less useful
fig=antipode_map_Robinson(X,Y,result, ShowOceans=True, ShowPoint=False, filename="./images/Antipodal_Lithosphere_Type_With_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, ShowOceans=True, ShowPoint=False, filename="./images/Antipodal_Lithosphere_Type_With_Oceans_Perspective.png")

# plot of just onland antipode classifications with default NE US reference point
fig=antipode_map_Robinson(X,Y,result, filename="./images/Antipodal_Lithosphere_Ohio_No_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, filename="./images/Antipodal_Lithosphere_Ohio_No_Oceans_Perspective.png")

# plot of all antipode classifications - with default NE US reference point
fig=antipode_map_Robinson(X,Y,result, ShowOceans=True, filename="./images/Antipodal_Lithosphere_Ohio_With_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, ShowOceans=True, filename="./images/Antipodal_Lithosphere_Ohio_With_Oceans_Perspective.png")

# plot of all just onland classifications - with a defined reference point in the UK
fig=antipode_map_Robinson(X,Y,result, Recenter=True, pointlat=51.80, pointlong=0.9, filename="./images/Antipodal_Lithosphere_UK_No_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, pointlat=51.80, pointlong=0.9, filename="./images/Antipodal_Lithosphere_UK_No_Oceans_Perspective.png")

# plot of all just onland classifications - with a defined reference point in South Africa
fig=antipode_map_Robinson(X,Y,result, Recenter=True, pointlat=-26.2, pointlong=28.0, filename="./images/Antipodal_Lithosphere_SA_No_Oceans_Robinson.png")
fig=antipode_map_Perspective(X,Y,result, pointlat=-26.2, pointlong=28.0, filename="./images/Antipodal_Lithosphere_SA_No_Oceans_Perspective.png")

