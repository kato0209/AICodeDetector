from airflow import models # This adds significant import time, so we import it here
from airflow.hooks.sqla_hook import initdb

def main():
    #Alembic from alembic.migration import MigrationContext log.info("Dropping tables that exist") models.base.Base.metadata.drop_all(settings.engine) mc = MigrationContext.configure(settings.engine) if mc._version.exists(settings.engine): mc._version.drop(settings.engine) from flask_appbuilder.models.sqla import Base Base.metadata.drop_all(settings.engine) initdb()