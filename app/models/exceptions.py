from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
#Ejercicio 1     
class FilmNotFound(Exception):

    def __init__(self, name = "Fil not found", description = 'Error film no encontrado'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 404
        print("erorr 404")

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
#Ejercicio 2    
class InvalidDataError(Exception):

    def __init__(self, name = "Error", description = 'error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 400
        print("erorr 400")

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response