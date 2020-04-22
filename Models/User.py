import hashlib
import uuid
from Database.Database import Database
from Models.Blog import Blog
from flask import session


class User(object):
    def __init__(self, password, email, name, _id=None):
        self._id = self.create_id() if _id is None else _id
        self.password = password
        self.email = email
        self.name = name

    def create_id(self):
        id = uuid.uuid4().hex
        data = self.get_by_id(id)
        if data is None:
            return id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one(collection='users', query={'email': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, id):
        data = Database.find_one(collection='users', query={'_id': id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        data = Database.find_one(collection='users', query={'email': email})
        if data is not None and data['password'] == str(hashlib.sha256(password.encode()).hexdigest()):
            User.login(email=email)
            return True
        else:
            return False

    @classmethod
    def register(cls, email, password, name):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email=email, password=password, name=name)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @staticmethod
    def login(email):
        session['email'] = email

    @staticmethod
    def logout(self):
        session['email'] = None

    def get_blogs(self):
        return Blog.get_by_user_id(self._id)

    def user_as_json(self):
        return {
            'email': self.email,
            '_id': self._id,
            'password': str(hashlib.sha256(self.password.encode()).hexdigest()),
            'name': self.name
        }

    def save_to_mongo(self):
        Database.insert("users", self.user_as_json())

    def create_blog(self, username, description):
        is_username = False
        blog = Database.find_one(collection='Blogs', query={'username': username})
        if blog is None:
            is_username = True
        id = uuid.uuid4().hex
        is_id = True
        blog = Database.find_one(collection='Blogs', query={'_id': id})
        if blog is not None:
            is_id = False
        while not is_id:
            id = uuid.uuid4().hex
            if Database.find(collection='Blogs', query={'_id': id}) is None:
                is_id = True
                break
        if is_username and is_id:
            Blog(author=self.name, username=username, _id=id, description=description, user_id=self._id).save_to_mongo()

    @staticmethod
    def new_post(self, username, content):
        blog_data = Database.find_one(collection='Blogs', query={'username': username})
        blog = Blog(author=blog_data['author'], username=blog_data['username'], _id=blog_data['_id'],
                    description=blog_data['description'], user_id=blog_data['user_id'])
        blog.new_post(title=username, content=content)

    def get_id(self):
        return self._id