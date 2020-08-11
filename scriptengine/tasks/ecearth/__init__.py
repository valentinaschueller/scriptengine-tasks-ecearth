""" ScriptEngine EC-Earth tasks

This module provides SE tasks for the EC-Earth ESM
"""

from .monitoring.simulated_legs import SimulatedLegs
from .monitoring.simulated_years import SimulatedYears
from .monitoring.write_scalar import WriteScalar
from .monitoring.markdown_output import MarkdownOutput
from .monitoring.global_average import GlobalAverage
from .monitoring.disk_usage import DiskUsage
from .monitoring.ice_volume import SeaIceVolume
from .monitoring.ice_area import SeaIceArea
from .monitoring.ocean_static_map import OceanStaticMap
from .monitoring.ocean_dynamic_map import OceanDynamicMap
from .monitoring.atmosphere_static_map import AtmosphereStaticMap
from .monitoring.atmosphere_dynamic_map import AtmosphereDynamicMap
from .monitoring.sithic_static_map import SithicStaticMap
from .monitoring.siconc_dynamic_map import SiconcDynamicMap
from .monitoring.atmosphere_time_series import AtmosphereTimeSeries
from .monitoring.sypd import SYPD
from .slurm import Sbatch

def task_loader_map():
    return {
        'sbatch': Sbatch,
        'ece.mon.sim_legs': SimulatedLegs,
        'ece.mon.sim_years': SimulatedYears,
        'ece.mon.write_scalar': WriteScalar,
        'ece.mon.markdown_report': MarkdownOutput,
        'ece.mon.global_avg': GlobalAverage,
        'ece.mon.disk_usage': DiskUsage,
        'ece.mon.ice_volume': SeaIceVolume,
        'ece.mon.ice_area': SeaIceArea,
        'ece.mon.ocean_static_map': OceanStaticMap,
        'ece.mon.ocean_dynamic_map': OceanDynamicMap,
        'ece.mon.atmosphere_static_map': AtmosphereStaticMap,
        'ece.mon.atmosphere_dynamic_map': AtmosphereDynamicMap,
        'ece.mon.sithic_static_map': SithicStaticMap,
        'ece.mon.siconc_dynamic_map': SiconcDynamicMap,
        'ece.mon.atmosphere_ts': AtmosphereTimeSeries,
        'ece.mon.sypd': SYPD,
        }
