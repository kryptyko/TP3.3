from flask import Blueprint
from ..models.exceptions import FilmNotFound, InvalidDataError
errors=Blueprint("errors",__name__)
@errors.app_errorhandler(FilmNotFound)
#ejercicio 3.3.1
def handle_FilmNotFound(error):
    return error.get_response() 
@errors.app_errorhandler(InvalidDataError)
def handle_InvalidDataRequest(error):
    return error.get_response()