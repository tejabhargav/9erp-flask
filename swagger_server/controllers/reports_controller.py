import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.report_data import ReportData  # noqa: E501
from swagger_server import util


def reports_get(report_type):  # noqa: E501
    """Generate reports

    Generate various reports (e.g., receipts report, pending fee report). # noqa: E501

    :param report_type: Type of report to generate
    :type report_type: str

    :rtype: ReportData
    """
    return 'do some magic!'
