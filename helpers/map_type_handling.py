"""Module containing plot functions for different map types."""

import warnings

import iris
import iris.quickplot as qplt
import iris.plot as iplt
import matplotlib.pyplot as plt
import cftime
import cf_units as unit
import math
import cartopy.crs as ccrs

def function_mapper(map_type_string):
    mapper = {
        'global ocean': global_ocean_plot,
    }
    return mapper.get(map_type_string, None)

def global_ocean_plot(cube, title=None, value_range=None, units=None):
    fig = plt.figure(figsize=(6,4), dpi=300)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    with warnings.catch_warnings():
        warnings.filterwarnings(
            action='ignore', 
            message="Coordinate system of latitude and longitude ", 
            category=UserWarning,
            )
        warnings.filterwarnings(
            action='ignore', 
            message="Coordinate 'projection_._coordinate' is", 
            category=UserWarning,
            )
        projected_cube, _ = iris.analysis.cartography.project(
            cube, 
            ccrs.PlateCarree(),
            nx=800,
            ny=400,
            )
        im = iplt.pcolormesh(
            projected_cube,
            axes=ax,
            vmin=value_range[0],
            vmax=value_range[1],
            )
    bar = fig.colorbar(im, orientation='horizontal')
    bar.set_label(units)
    ax.set_title(title)
    ax.coastlines()
    return fig

    