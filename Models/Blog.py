import uuid
import hashlib
from Database.Database import Database
from Models.Post import Post


class Blog(object):
    def __init__(self, author, username, _id, description, user_id):
        self.author = author
        self.username = username
        self._id = uuid.uuid4().hex if _id is None else _id
        self.description = description
        self.user_id = user_id

    def new_post(self, title, content):
        author = self.author
        _id = self._id
        Post(blog_id=_id, title=title, content=content, author=author).save_to_mongo()

    def get_posts(self):
        return Post.from_blog(id=self._id)

    def save_to_mongo(self):
        Database.insert(collection='Blogs', data=self.blog_as_json())

    def blog_as_json(self):
        return {
            'author': self.author,
            '_id': self._id,
            'username': self.username,
            'description': self.description,
            'user_id': self.user_id
        }

    @classmethod
    def get_by_user_id(cls, id):
        return [cls(**blog_data) for blog_data in Database.find(collection='Blogs', query={'user_id': id})]

    @classmethod
    def get_by_id(cls, id):
        blog_data = Database.find_one(collection='Blogs', query={'_id': id})
        return cls(**blog_data)