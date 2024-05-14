from airflow import settings, tasks
import time
t = tasks.init_app(settings.APPS)

def initdb(): # alembic adds a variable to import time, so we import it lazily from alembic.migration import MigrationContext log.info("Dropping tables that exist") models.base.Base.metadata.drop_all(settings.engine) mc = MigrationContext.configure(settings.engine) if mc._version.exists(settings.engine): mc._version.drop(settings.engine) from flask_appbuilder.models.sqla import Base Base.metadata.drop_all(settings.engine) initdb()