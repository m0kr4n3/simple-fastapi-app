# simple-fastapi-app
Simple RESTful application with FastAPI + MongoDB + JWT + Docker


## Features
- Docker with [MongoDB](https://mongodb.com/) and [FastAPI](https://fastapi.tiangolo.com/).
- Authentication and securing some routes with [JWT tokens](https://jwt.io/)
- Works well async (all, even db calls thanks to [motor](https://motor.readthedocs.io/en/stable/))

Built on Python: 3.8.

## File Structure
```
.
├── app
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── src
│       ├── auth
│           ├── auth_bearer.py
│           └── auth_handler.py
│       ├── models
│           ├── post.py
│           ├── user.py
│           └── student.py
│       ├── routes
│           ├── post.py
│           ├── user.py
│           └── student.py
│       ├── api.py
│       └── database.py
└── docker-compose.yml
```

## Installation and usage
- Create env from template:
```bash
cp example.env .env #only once
```
- Run docker-compose:
```bash
sudo docker-compose up
```

## References
- [Building a CRUD App with FastAPI and MongoDB](https://testdriven.io/blog/fastapi-mongo/#crud-routes)
- [Securing FastAPI with JWT Token-based Authentication](https://testdriven.io/blog/fastapi-jwt-auth/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
