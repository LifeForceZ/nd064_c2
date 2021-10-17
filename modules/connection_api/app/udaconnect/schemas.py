from app.udaconnect.models import Connection

import sys
sys.path.append('../')

from location_api.app.udaconnect.schemas import LocationSchema
from person_api.app.udaconnect.schemas import PersonSchema

from geoalchemy2.types import Geometry as GeometryType
from marshmallow import Schema, fields
from marshmallow_sqlalchemy.convert import ModelConverter as BaseModelConverter

class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
