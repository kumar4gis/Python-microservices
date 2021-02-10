#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install MicroServicesApp


# In[ ]:


pip install flask


# In[ ]:


from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)

enabled_modules = [
    # Normally, we'd define more modules to enable:

    # 'home',
    # 'forum',
    # 'settings',

    # We will enable just one, for now:

    'admin'
]

# By default, this will assume your modules directory is "./modules" if a second argument is not provided.
app.register_urls(enabled_modules)
app.run()


# In[ ]:


pip install flask_microservices


# In[ ]:


from flask_microservices import MicroServicesApp

app = MicroServicesApp(__name__)

enabled_modules = [
    # Normally, we'd define more modules to enable:

    # 'home',
    # 'forum',
    # 'settings',

    # We will enable just one, for now:

    'admin'
]

# By default, this will assume your modules directory is "./modules" if a second argument is not provided.
app.register_urls(enabled_modules)
app.run()


# In[ ]:


import json


class Book:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)

    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                index = idx
                found = True
                del self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)


# In[ ]:


from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)


# In[ ]:


from time import sleep

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}! (version 2)".format(name)


# In[ ]:


#~/movie_service/app/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {"Real": "Python"}


# In[ ]:


#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()


# In[ ]:


#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)


# In[1]:


from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)


# In[4]:


pip install nameko


# In[5]:


pip install nameko


# In[1]:


from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)


# In[3]:


from time import sleep

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}!".format(name)


# In[4]:


from time import sleep

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}!".format(name)


# In[15]:


GreetingService.hello(1,name='world')
    


# In[13]:


from flask import Flask
app=flask(_new_)
@app.route('/')
def hellow_world():
    return "Hello world"

if __name=='__main__':
 app.run()


# In[ ]:




