from .monitoring.simulated_legs import SimulatedLegs
from .monitoring.simulated_years import SimulatedYears
from .monitoring.write_scalar import WriteScalar
from .monitoring.markdown_output import MarkdownOutput
from .monitoring.global_average import GlobalAverage
from .monitoring.disk_usage import DiskUsage
from .monitoring.ice_volume import IceVolume

def task_loader_map():
    return {
        'ece.mon.sim_legs': SimulatedLegs,
        'ece.mon.sim_years': SimulatedYears,
        'ece.mon.write_scalar': WriteScalar,
        'ece.mon.markdown_report': MarkdownOutput,
        'ece.mon.global_avg': GlobalAverage,
        'ece.mon.disk_usage': DiskUsage,
        'ece.mon.ice_volume': IceVolume,
        }