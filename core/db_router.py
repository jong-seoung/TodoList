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
        기본 데이터베이스와 읽기 전용 데이터베이스 간의 관계를 허용합니다.
        """
        db_list = ('default', 'replica')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up on the primary database (모든 마이그레이션 작업은 기본 데이터베이스로 전달).
        """
        return db == 'default'
