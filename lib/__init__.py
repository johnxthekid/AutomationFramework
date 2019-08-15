from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), ".."))
print(sys.path)

from logging import config

report_dir = path.join(path.dirname(__file__), "..", "report", "logging.conf")

# config.fileConfig(report_dir)