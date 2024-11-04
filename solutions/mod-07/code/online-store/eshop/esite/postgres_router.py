class PostgresRouter:
    """
    A router to control all database operations on models in the applications.
    """

    route_app_labels = {"auth", "products", }

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and products models go to 'postgres'.
        """
        if model._meta.app_label in self.route_app_labels:
            return "postgres"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and products models go to 'postgres'.
        """
        if model._meta.app_label in self.route_app_labels:
            return "postgres"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or products apps is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and products apps only appear in the 'postgres' database.
        """
        if app_label in self.route_app_labels:
            return db == "postgres"
        return None
