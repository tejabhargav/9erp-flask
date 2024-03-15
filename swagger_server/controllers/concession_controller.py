import connexion
import six

from swagger_server.models import (
    AddConcessionRequest,
    Error,
    Response
)
from swagger_server import util
from swagger_server.__main__ import mongo
from loguru import logger

def concession_add(body):  # noqa: E501
    """Add concession

    Add concession # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = AddConcessionRequest.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            logger.info("concession_add")
            
            # creating an id for the concession
            id_type = 'CON'
            last_sequence = mongo.db.idTypeSequences.find_one(
                {'idType': id_type}
            )
            if not last_sequence:
                mongo.db.idTypeSequences.insert_one(
                    {
                        'idType': id_type,
                        'lastSequence': '90000',
                    }
                )
                last_sequence = mongo.db.idTypeSequences.find_one(
                    {'idType': id_type}
                )
            
            concession_custom_id = util.generate_custom_id(
                id_type,
                last_sequence['lastSequence']
            )
            
            mongo.db.idTypeSequences.update_one(
                {'idType': id_type},
                {
                    '$set': {
                        'lastSequence': concession_custom_id['updatedSequence'],
                    }
                }
            )
            
            concession_id = concession_custom_id['id']
            
            mongo.db.concessions.insert_one(
                {
                    'concessionId': concession_id,
                    'applicationNumber': body.application_number,
                    'studentName': body.student_name,
                    'feeType': body.fee_type,
                    'amount': body.amount,
                    'reason': body.reason,
                    'issuedBy': body.issued_by,
                    'issuedDate': body.issued_date,
                }
            )
            
            added_concession = mongo.db.concessions.find_one(
                {'concessionId': concession_id},{"_id": 0}
            )
            
            if added_concession is None:
                raise Exception("Concession not added")

            return Response(
                message="Concession added successfully",
                data=added_concession
            )
        except Exception as e:
            logger.error(e)
            return Error(
                message="Internal server error"
            )