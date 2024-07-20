import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
						"packages": ['os', 'pendulum', 'pandas', 'selenium'], 
						"excludes": [],
						"include_msvcr": True
					}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

version = "10.0"
setup(  name = f"Whatspp Alert APP{version}",
        version = version,
        description = f"Whatspp Alert APP{version}",
        options = {"build_exe": build_exe_options},
        executables = [Executable(f"Whatspp Alert APP")])
