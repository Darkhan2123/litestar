from piccolo.apps.user.tables import BaseUser
from piccolo.columns import Boolean, ForeignKey, Timestamp, Varchar, Serial
from piccolo.columns.readable import Readable
from piccolo.table import Table
from datetime import datetime

class Task(Table, tablename="tasks"):
    '''
    Task table with improved field definitions
    '''
    id = Serial(primary_key=True)
    name = Varchar(length=255)
    completed = Boolean(default=False)
    created_at = Timestamp(default=datetime.now)
    task_user = ForeignKey(BaseUser)

    @classmethod
    def get_readable(cls):
        return Readable(template='%s', columns=[cls.task_user.username])
