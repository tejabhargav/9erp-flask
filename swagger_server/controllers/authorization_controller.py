import connexion
from loguru import logger
from typing import List
from swagger_server.models import LoginRequest, Employee, Response
from swagger_server.__main__ import mongo
from swagger_server import util

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_bearerAuth(token):
    return {'test_key': 'test_value'}


def login(body):
    try:
        if connexion.request.is_json:
            body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
            logger.info('Login API has been called ')
            
            employee = Employee.from_dict(mongo.db.employees.find_one(
                {"email": body.username, "password": body.password}))
            
            if employee is None:
                raise Exception("Invalid username or password")

            return Response(
                data={
                    'employeeRole': employee.role,
                    'employeeName': employee.employee_name,
                    'employeeBranch': employee.branch,
                    'employeeUsername': employee.username
                },
                message="Login Successful",
            )
    except Exception as e:
        logger.error(e)
        return Response(
            data={},
            message="Login Failed",
            error=str(e)
        )