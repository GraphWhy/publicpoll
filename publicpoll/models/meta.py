from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    # Index
    "ix": "ix_%(column_0_label)s",
    # unique constraint
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    # Check Constraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # Foreign Key 
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    # Primary Key Constraint
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)
