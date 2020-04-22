from Database.Database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), post_id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.post_id = uuid.uuid4().hex if post_id is None else post_id
        self.created_date = created_date

    def save_to_mongo(self):
        Database.insert('posts', self.post_as_json())

    def post_as_json(self):
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'blog_id': self.blog_id,
            'post_id': self.post_id,
            'created_date': self.created_date
        }

    @classmethod
    def get_by_title(cls, title=None):
        if title is None:
            return [data for data in Database.find(collection='posts', query={})]
        else:
            data = Database.find_one(collection='posts', query={'title': title})
            return cls(**data)

    @staticmethod
    def get_by_blog_id(_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': _id})]
