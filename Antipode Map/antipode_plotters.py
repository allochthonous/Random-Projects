#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:05:24 2023

Routines for plotting antipode grid in either Robinson or paired Nearside
Perspective projections. Includes options to just plot grid on continents and
show location and antipode of a chosen point.  

@author: crowan
"""

import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

bicolormap=ListedColormap(["#2c7fb8", "#edf8b1"])

def antipode_map_Robinson(X, Y, categorygrid, ShowOceans=False, 
                          ShowPoint=True, pointlat=41.15, pointlong=-81.36, 
                          Recenter=False, filename=None): 
    """
    Plots global map of antipodal lithosphere types, Robinson projection.

    Parameters
    ----------
    X : numpy array. X coordinates from product of numpy.meshgrid(longs, lats)
    Y : numpy array. Y coordinates from product of numpy.meshgrid(longs, lats)
    categorygrid : numpy array with dimensions X,Y: antipode classification values
    ShowOceans : True/False, optional
        If True, grid is also displayed in ocean basins as well as continents. 
        The default is False.
    ShowPoint : True/False, optional
        If True, displays a user-defined point (solid red triangle) and its antipode 
        (open triangle) on the nap. The default is True.
    pointlat : FLOAT, optional
        latitude of point to display. The default is 41.15 (NE US).
    pointlong : FLOAT, optional
        longitude of point to display. The default is -81.36 (NE US).
    Recenter : True/False, optional
        If True, central longitude of map (usually 0 E) will be average of point 
        and antipodal longitudes. Useful for when point or antipode is close to 0 or +/i 180 E. 
        The default is False.
    filename : STRING optional
        If a filename is given, then a png of the plot will be saved to disk. The default is None.

    Returns
    -------
    fig : matplotlib figure

    """
    # find antipodal latitude
    if pointlong>0: long2=pointlong-180
    else: long2=pointlong+180 
    # initial legend includes only -> ocean and -> continent patches 
    legend_elements = [Patch(color='none', label='Antipode:'),
                       Patch(facecolor="#2c7fb8", label='in oceans'),
                       Patch(facecolor="#edf8b1", label='on continent')
                       ]
    cols=3
    legendpad=0.03
    # if recentering, central longitude will be average of point and antipodal longitudes
    if Recenter==True:
        centroid=0.5*(pointlong+long2)
    else: centroid=0.0
    # easier to have 0 as the lowest value for a colormap, and collapsing to 2 categories 
    # (->continent and -> ocean) rather than 4 when displaying oceans makes things less confusing.
    if ShowOceans==False:
        categorygrid=np.where(categorygrid<=2, categorygrid-1, np.nan)
    else:
        categorygrid=np.where((categorygrid>1) & (categorygrid<4), 1, 0)
        
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1, projection=ccrs.Robinson(central_longitude=centroid))
    ax.pcolormesh(X, Y, categorygrid, shading='auto', cmap=bicolormap, transform=ccrs.PlateCarree())
    ax.coastlines(lw=0.8, color='0.1')
    if ShowOceans==False:
        ax.add_feature(cfeature.OCEAN, color='0.95', zorder=1)
    if ShowPoint==True:
        plt.scatter([pointlong, long2], [pointlat, -pointlat], marker='^', color='red', 
                    facecolor=['red','white'], s=50, transform=ccrs.PlateCarree(), zorder=2)
        # add additional legend elements for point and antipode
        legend_elements.append(Patch(color='none', label=''),)
        legend_elements.append(Line2D([0], [0], marker='^', color='w', markeredgecolor='red', markerfacecolor='red', 
                                      label=("%s E, %s N" % (np.round(pointlong,1),np.round(pointlat,1))), markersize=8))
        legend_elements.append(Line2D([0], [0], marker='^', color='w', markeredgecolor='red', markerfacecolor='white', 
                                      label='Antipode', markersize=8))
        cols=2
        legendpad=-0.05
    plt.title('Global map of antipodal lithosphere type', weight='bold', pad=10)    
    fig.legend(handles=legend_elements, ncols=cols, loc=8, bbox_to_anchor=(0.5,legendpad),fontsize=8)
    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=800, bbox_inches='tight')
    return fig

def antipode_map_Perspective(X, Y, categorygrid, ShowOceans=False, 
                          ShowPoint=True, pointlat=41.15, pointlong=-81.36, 
                          filename=None):  
    """
    Plots global map of antipodal lithosphere types, 2 NearSide Perspective Projections
    centered on the specified point and its antipode.

    Parameters
    ----------
    X : numpy array. X coordinates from product of numpy.meshgrid(longs, lats)
    Y : numpy array. Y coordinates from product of numpy.meshgrid(longs, lats)
    categorygrid : numpy array with dimensions X,Y: antipode classification values
    ShowOceans : True/False, optional
        If True, grid is also displayed in ocean basins as well as continents. 
        The default is False.
    ShowPoint : True/False, optional
        If True, displays a user-defined point (solid red triangle) and its antipode 
        (open triangle) on the nap. The default is True.
    pointlat : FLOAT, optional
        latitude of point to display. The default is 41.15 (NE US).
    pointlong : FLOAT, optional
        longitude of point to display. The default is -81.36 (NE US).
    filename : STRING optional
        If a filename is given, then a png of the plot will be saved to disk. The default is None.

    Returns
    -------
    fig : matplotlib figure

    """
    if pointlong>0: long2=pointlong-180
    else: long2=pointlong+180 

    legend_elements = [Patch(color='none', label='Antipode:'),
                       Patch(facecolor="#2c7fb8", label='in oceans'),
                       Patch(facecolor="#edf8b1", label='on continent')
                       ]
    cols=3
    legendpad=0

    if ShowOceans==False:
        categorygrid=np.where(categorygrid<=2, categorygrid-1, np.nan)
    else:
        categorygrid=np.where((categorygrid>1) & (categorygrid<4), 1, 0)

    fig = plt.figure()
    fig.suptitle('Global map of antipodal lithosphere type', weight='bold', y=0.9)    
    ax1 = fig.add_subplot(1,2,1, projection=ccrs.NearsidePerspective(central_longitude=pointlong, central_latitude=pointlat))
    ax2 = fig.add_subplot(1,2,2, projection=ccrs.NearsidePerspective(central_longitude=long2, central_latitude=-pointlat))

    ax1.pcolormesh(X, Y, categorygrid, shading='auto', cmap=bicolormap, transform=ccrs.PlateCarree())
    ax2.pcolormesh(X, Y, categorygrid, shading='auto', cmap=bicolormap, transform=ccrs.PlateCarree())

    ax1.coastlines(lw=0.8, color='0.1')
    ax2.coastlines(lw=0.8, color='0.1')
    ax1.gridlines(lw=0.5, linestyle=':')
    ax2.gridlines(lw=0.5, linestyle=':')
    
    if ShowOceans==False:
        ax1.add_feature(cfeature.OCEAN, color='0.95', zorder=1)
        ax2.add_feature(cfeature.OCEAN, color='0.95', zorder=1)
    if ShowPoint==True:
        ax1.scatter([pointlong, long2], [pointlat, -pointlat], marker='^', color='red', 
                    facecolor=['red','white'], s=50, transform=ccrs.PlateCarree(), zorder=2)
        ax2.scatter([pointlong, long2], [pointlat, -pointlat], marker='^', color='red', 
                    facecolor=['red','white'], s=50, transform=ccrs.PlateCarree(), zorder=2)
        
        legend_elements.append(Patch(color='none', label=''),)
        legend_elements.append(Line2D([0], [0], marker='^', color='w', markeredgecolor='red', markerfacecolor='red', 
                                      label=("%s E, %s N" % (np.round(pointlong,1),np.round(pointlat,1))), markersize=8))
        legend_elements.append(Line2D([0], [0], marker='^', color='w', markeredgecolor='red', markerfacecolor='white', 
                                      label='Antipode', markersize=8))
        cols=2
        legendpad=-0.08

    fig.legend(handles=legend_elements, ncols=cols, loc=8, bbox_to_anchor=(0.5,legendpad),fontsize=8)
    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=800, bbox_inches='tight')
    return fig