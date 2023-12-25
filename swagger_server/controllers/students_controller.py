import connexion
import six
import datetime
from loguru import logger
from swagger_server.__main__ import mongo
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.models.student_create_request import StudentCreateRequest  # noqa: E501
from swagger_server.models.student_list import StudentList  # noqa: E501
from swagger_server.models.student_update_request import StudentUpdateRequest  # noqa: E501
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
        logger.info("Creating student")
        body = StudentCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if mongo.db.students.find_one(
                {'application_number': body.application_number}
            ):
                logger.error(f"Student with application number {body.application_number} already exists")
                return Error(
                    message=f"Student with application number {body.application_number} already exists"
                )
            last_sequence = mongo.db.idTypeSequences.find_one(
                {'idType': 'STU'}
            )
            time_now = datetime.datetime.now()
            if not last_sequence:
                mongo.db.idTypeSequences.insert_one(
                    {
                        'idType': 'STU',
                        'lastSequence': '0000',
                        'lastUpdated': time_now
                    }
                )
                last_sequence = mongo.db.idTypeSequences.find_one(
                    {'idType': 'STU'}
                )
            
            student_custom_id = util.generate_custom_id(
                'STU',
                last_sequence['lastSequence']
            )
            
            mongo.db.idTypeSequences.update_one(
                {'idType': 'STU'},
                {
                    '$set': {
                        'lastSequence': student_custom_id['updatedSequence'],
                        'lastUpdated': time_now
                    }
                }
            )
            
            student = Student(
                student_id=student_custom_id['id'],
                name=body.name,
                application_number=body.application_number,
                date_of_joining=datetime.date.today().isoformat(),
                branch=body.branch,
                parent_name=body.parent_name,
                primary_number=body.primary_number,
                secondary_number=body.secondary_number,
                gender=body.gender,
                batch=body.batch,
                year_of_joining=body.year_of_joining,
                section=body.section,
                roll_number=body.roll_number,
                fee_structure_for_one_year=body.fee_structure_for_one_year,
            )
                
            mongo.db.students.insert_one((util.snake_to_camel(student.to_dict())))
            create_student_response = Student.from_dict(mongo.db.students.find_one(
                {'studentId': student_custom_id['id']}
            ))
            if create_student_response.student_id == student_custom_id['id']:
                
                logger.info(f"Student created successfully with ID: {student_custom_id['id']}")
                return student
            
            return Error(
                message='Student creation failed'
            )
        except Exception as e:
            logger.error(f"Error creating student: {e}")
            return Error(
                message='Student creation failed'
            )


def students_student_id_put(body, student_id):  # noqa: E501
    """Update student details

    Update details of an existing student by ID. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param student_id: ID of the student to update
    :type student_id: str

    :rtype: Student
    """
    if connexion.request.is_json:
        body = StudentUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
