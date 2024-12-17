from app.db.postgres.database_config import session_maker
from app.db.postgres.models import Department


def get_or_insert(department: Department) -> Department:
    with session_maker() as session:
        found = session.query(Department).filter(Department.name == department.name).one_or_none()
        if found:
            return found
        else:
            session.add(department)
            session.commit()
            session.refresh(department)
            return department
