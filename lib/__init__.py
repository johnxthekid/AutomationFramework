from os import path
from logging import config

report_dir = path.join(path.dirname(__file__), "..", "report", "logging.conf")

# config.fileConfig(report_dir)