"""class AppRouter:
    def db_for_read(self, model, **hints):
        # Specify the database for reading
        return 'second_db' if model._meta.app_label == 'second_app' else None

    def db_for_write(self, model, **hints):
        # Specify the database for writing
        return 'second_db' if model._meta.app_label == 'second_app' else None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the 'your_app_label' app
        if obj1._meta.app_label == 'second_app' and obj2._meta.app_label == 'second_app':
            return True
        # Allow relations if both objects are not in the 'your_app_label' app
        elif 'second_app' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations only for the 'your_app_label' app on the 'second_db'
        if app_label == 'second_app':
            return db == 'second_db'
        return None"""


class AppRouter:
    
    def db_for_read(self, model, **hints):
        print("---------------allow_migrate------------------")
        # Specify the database for reading
        return 'second_db' if model._meta.app_label == 'second_app' else None

    def db_for_write(self, model, **hints):
        # Specify the database for writing
        return 'second_db' if model._meta.app_label == 'second_app' else None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the 'second_app' app
        if obj1._meta.app_label == 'second_app' and obj2._meta.app_label == 'second_app':
            return True
        # Allow relations if both objects are not in the 'second_app' app
        elif 'second_app' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return None

    def allow_migrate(self, db, app_label,model=None, **hints):
        # Allow migrations only for the 'second_app' app on the 'second_db'
        print("---------------allow_migrate------------------")
        if app_label == 'second_app':
            return db == 'second_db'
        return False