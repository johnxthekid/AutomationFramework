import os

from robot.rebot import rebot
from robot.api import ExecutionResult, ResultVisitor
from tkinter import filedialog, Tk, messagebox


class RobotReportGenerator:

    @staticmethod
    def get_root_folder():
        root = Tk()
        root.withdraw()
        return filedialog.askdirectory(title="Please select output report folder")

    @staticmethod
    def get_xml_files(folder_path):
        xml_files = []
        for root, directory, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.xml') and file.startswith('output'):
                    xml_files.append(os.path.join(root, file))

        return xml_files

    @staticmethod
    def get_test_status(*xml_files):
        for xml_file in xml_files:
            result = ExecutionResult(xml_file)
            result.visit(GetResults(xml_file))

    @staticmethod
    def updatepassedresults(report, output_name='common_passed.xml'):
        end_result = ExecutionResult(report)
        end_result.visit(UpdateResultsBaseOnPass(results=end_result))
        end_result.save(output_name)

    @classmethod
    def generate_report(cls, *output_reports, name="Test Application", outputdir=None, update_if_pass=True):

        rebot(*output_reports, name=name.strip().replace(' ', '_'), merge=True, outputdir=os.getcwd()
            if outputdir is not None else outputdir, output='combine_output.xml',
              log='combine_log.xml', report='combine_report.xml')

        if update_if_pass:
            RobotReportGenerator.get_test_status(*output_reports)
            RobotReportGenerator.updatepassedresults('combine_output.xml')

            rebot(*output_reports, name=name.strip().replace(' ', '_'), merge=True, outputdir=os.getcwd()
            if outputdir is not None else outputdir, output='combine_output.xml',
                  log='combine_log.xml', report='combine_report.xml')


class GetResults(ResultVisitor):

    def __init__(self, path):
        self.path = path

    def visit_test(self, test):
        return {self.path: {test.name: {'status': test.status, 'id': test.id, 'message': test.message}}}


class UpdateResultsBaseOnPass(ResultVisitor):

    def __init__(self, results):
        self.results = results

    def visit_test(self, test):
        if test.status == 'FAIL':
            for report in self.results:
                if test.name in self.results[report] and self.results[report][test.name]['status'] == 'PASS':
                    test.status = 'PASS'
                    test.message = f'Test PASSED in report: {report} \n{self.results[report][test.name]["status"]}'
                    break


if __name__ == '__main__':
    rpg = RobotReportGenerator()
    rd = rpg.get_root_folder()
    xml_list = rpg.get_xml_files(rd)
    rpg.generate_report(*xml_list, name="Sample Report Combine", outputdir=rd)

    # todo: make it work with different root directories