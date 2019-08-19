import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from robot.api import logger

from lib.frontend.apphelpers.SampleNotepadHelper import SampleNotepadHelper
from lib.browsers.pageobjectmodels.DemoMainPage import DemoMainPage


class AllKeywordsLibrary(DemoMainPage, SampleNotepadHelper):

    def __init__(self, run_location):
        logger.info(f"Running keyword library: {run_location}")
        SampleNotepadHelper.__init__(self)
        DemoMainPage.__init__(self)