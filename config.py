class Config:
    SECRET_KEY = "secretkey123"

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:password@localhost/taskmanager"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
