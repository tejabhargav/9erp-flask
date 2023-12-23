import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.models.student_create_request import StudentCreateRequest  # noqa: E501
from swagger_server.models.student_list import StudentList  # noqa: E501
from swagger_server import util


def students_delete(student_id):  # noqa: E501
    """Delete a student

    Delete a student by ID. # noqa: E501

    :param student_id: ID of the student to delete
    :type student_id: str

    :rtype: None
    """
    return 'do some magic!'


def students_get():  # noqa: E501
    """Retrieve all students

    Get a list of all students. # noqa: E501


    :rtype: StudentList
    """
    return 'do some magic!'


def students_post(body):  # noqa: E501
    """Create a new student

    Add a new student to the system. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Student
    """
    if connexion.request.is_json:
        body = StudentCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
