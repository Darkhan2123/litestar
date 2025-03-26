import os
from piccolo.conf.apps import AppConfig
from apps.tasks.tables import Task

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

APP_CONFIG = AppConfig(
    app_name="tasks",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, 'piccolo_migrations'),
    table_classes=[Task],
    migration_dependencies=[],
    commands=[],
)
