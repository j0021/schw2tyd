from setuptools import setup

setup(
    name="schw2tyd",
    version="0.0.2",
    py_modules=["schw2tyd"],
    entry_points={
        "console_scripts":[
            "schw2tyd=schw2tyd:main"
        ]
    }
)
