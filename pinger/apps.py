from django.apps import AppConfig
from django.db import connection


class PingerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pinger'

    def ready(self):
        super().ready()
        if connection.connection is not None and connection.has_table('pinger_domain'):
            from pinger.ping import DomainPingController
            ping_controller = DomainPingController()
            ping_controller.start()

