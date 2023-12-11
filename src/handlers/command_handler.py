from src.models.user import User
from src.models.repository.user_repository import UserRepository
import bcrypt
from flask import jsonify

class CommandHandler:
    def __init__(self, user: User = None):
        self._user_repo = UserRepository()
        
    def receive_data_to_insert_or_update(self, method_name, request_data: dict):
        method = getattr(self, method_name)
        return method(User(**request_data))
    
    def insert_new_user(self, user_dict: dict):
        user = User(**user_dict)
        self._user_repo.insert_one(user)
        user_response = {
            'name' : user.name,
            'last_name' : user.last_name,
            'age' : user.age,
            'user_name' : user.user_name,
            'email' : user.email
        }
        return user_response
    
    def find_user_by_email(self, email_request: dict):
        filter = email_request
        print(filter)
        return self._user_repo.find_one(filter)
    
    def test_mongo(self):
        print(self._user_repo.test_mongo())
        return self._user_repo.test_mongo()
    
    def login(self, user_email: dict):
        if not user_email: return {}
        password_before = user_email.get('password', '')
        filter = { 'email' : user_email.get('email', '')}
        user_from_mogo = self._user_repo.find_one_for_login(filter)
        print(user_from_mogo)
        print("aja" , user_from_mogo and self._user_repo.validate_user_password(password_before, user_from_mogo.get('password', '')))
        if user_from_mogo and self._user_repo.validate_user_password(password_before, user_from_mogo.get('password', '')):
            request = jsonify(
                {'name': user_from_mogo.get('name'),
                'email': user_from_mogo.get('email'),
                'user_name': user_from_mogo.get('user_name'),
                'staus': 'OK',
                'message': 'Login Successfull'}
            )
            return request
        bad_request = jsonify(
                    {'name': '',
                    'email': '',
                    'user_name': '',
                    'staus': 'ERROR',
                    'message': 'Login Unsuccessfull'}
        )
        bad_request.status_code = 404
        return bad_request
        
        