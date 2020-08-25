"""Processing Task that writes out the disk usage of a given folder."""
import os

from scriptengine.tasks.base.timing import timed_runner
from .scalar import Scalar

class DiskusageRteScalar(Scalar):
    """DiskusageRteScalar Processing Task"""
    def __init__(self, parameters):
        required = [
            "src",
            "dst",
        ]
        super(Scalar, self).__init__(__name__, parameters, required_parameters=required)

    @timed_runner
    def run(self, context):
        src = self.getarg('src', context)
        dst = self.getarg('dst', context)
        self.log_info(f"Write disk usage of {src} to {dst}")

        value = round(self.get_directory_size(src) * 1e-9, 1)
        self.log_debug(f"Size of Directory: {value}")

        self.save(
            dst,
            title="Disk Usage in GB",
            comment=f"Current size of {src}.",
            data=value,
            diagnostic_type=self.diagnostic_type,
        )

    def get_directory_size(self, path):
        """Returns the size of `path` in Bytes."""
        self.log_debug("Getting directory size.")
        total = 0
        try:
            for entry in os.scandir(path):
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.get_directory_size(entry.path)
        except NotADirectoryError:
            self.log_warning(f"{path} is not a directory. Returning -1.")
            return -1e9 # gets multiplied with 1e-9 again
        except PermissionError:
            self.log_warning(f"No permission to open {path}. Returning -1.")
            return -1e9 # gets multiplied with 1e-9 again

        return total
