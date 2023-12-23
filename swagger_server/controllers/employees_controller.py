import connexion
import six

from swagger_server.models.employee import Employee  # noqa: E501
from swagger_server.models.employee_create_request import EmployeeCreateRequest  # noqa: E501
from swagger_server.models.employee_list import EmployeeList  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def employees_delete(employee_id):  # noqa: E501
    """Delete an employee

    Delete an employee by ID. # noqa: E501

    :param employee_id: ID of the employee to delete
    :type employee_id: str

    :rtype: None
    """
    return 'do some magic!'


def employees_get():  # noqa: E501
    """Retrieve all employees

    Get a list of all employees. # noqa: E501


    :rtype: EmployeeList
    """
    return 'do some magic!'


def employees_post(body):  # noqa: E501
    """Create a new employee

    Add a new employee to the system. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        body = EmployeeCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
