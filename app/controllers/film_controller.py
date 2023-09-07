from ..models.film_model import Film
from app.models.exceptions import FilmNotFound, InvalidDataError
from flask import request

from decimal import Decimal 

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)
        print(result)
        if result is not None:
            return result.serialize(), 200
        else:
            raise FilmNotFound(film_id)
            
        
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        #ejercicio2
        # TODO: Validate data
        if len(data['title']) <= 3:
            raise InvalidDataError('El título debe tener más de 3 caracteres')
        if not isinstance(data.get('language_id'), int):
            raise InvalidDataError('language_id debe ser un número entero')

        if not isinstance(data.get('rental_duration'), int):
            raise InvalidDataError('rental_duration debe ser un número entero')

        if not isinstance(data.get('rental_rate'), int):
            raise InvalidDataError('rental_rate debe ser un número entero')

        if not isinstance(data.get('replacement_cost'), int):
            raise InvalidDataError('replacement_cost debe ser un número entero')

        valid_special_features = [
            'Trailers',
            'Commentaries',
            'Deleted Scenes',
            'Behind the Scenes'
        ]
        special_features = data.get('special_features', [])
        if not isinstance(special_features, list) or not all(feature in valid_special_features for feature in special_features):
            raise InvalidDataError('special_features debe ser una lista de cadenas válidas')
        #fin codigo ejercicio2
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        film = Film(**data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json
        # TODO: Validate data
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        Film.update(film)
        return {'message': 'Film updated successfully'}, 200
    
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        Film.delete(film)
        return {'message': 'Film deleted successfully'}, 204