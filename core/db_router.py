class PrimaryReplicaRouter:
    """
    A router to control all database operations on models for
    primary/replica (write/read) setup.
    """

    def db_for_read(self, model, **hints):
        """
        Directs read operations to the replica (읽기 전용 데이터베이스로 읽기 작업을 전달).
        """
        return 'replica'

    def db_for_write(self, model, **hints):
        """
        Directs write operations to the primary (기본 데이터베이스로 쓰기 작업을 전달).
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allows relations if a model is in the primary/replica (읽기/쓰기 데이터베이스 간의 관계 허용 여부).
        """
        db_obj1 = hints.get('instance', obj1)._state.db
        db_obj2 = hints.get('instance', obj2)._state.db
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up on the primary database (모든 마이그레이션 작업은 기본 데이터베이스로 전달).
        """
        return db == 'default'
