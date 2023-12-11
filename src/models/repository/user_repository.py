from src.db.client import ClientDB
from src.models.user import User
import bcrypt

class UserRepository:
    def __init__(self) -> None:
        self.COLLECTION_NAME = "users"
        self._cdb = ClientDB()
    
    def insert_one(self, user: User):
        hashed_passoword = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user_dict = {
            'name' : user.name,
            'last_name' : user.last_name,
            'age' : user.age,
            'user_name' : user.user_name,
            'email' : user.email,
            'password' : hashed_passoword
        }
        #self._user_repo.insert_one(user_dict)
        # user_find = self.find_user_by_email({'email': user.email})
        # print(user_find.get('password'))
        # decrypt_pass = bcrypt.checkpw(bytes('keew33', 'utf-8'), user_find.get('password'))
        # print(decrypt_pass)
        return self._cdb.insert_one(self.COLLECTION_NAME, user_dict)
        
    def find_one(self, filter):
        return self._cdb.find_one(self.COLLECTION_NAME, filter)
    
    def find_one_for_login(self, filter):
        return self._cdb.find_one_for_login(self.COLLECTION_NAME, filter)
    
    def validate_user_password(self, password_typing, password_mongo):
        print(password_mongo)
        decrypt_pass = bcrypt.checkpw(bytes(password_typing, 'utf-8'), password_mongo)
        print(decrypt_pass)
        if decrypt_pass: return True
        
        return False
    
    
    def test_mongo(self):
        print()
        return self._cdb.test_mongo(self.COLLECTION_NAME)
    