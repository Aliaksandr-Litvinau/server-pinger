import threading
import time
import requests
import logging
from datetime import datetime

from config import settings
from .models import Domain, ResponseTime

logger = logging.getLogger(__name__)


class DomainPingController:
    def __init__(self):
        self.interval = getattr(settings, 'PING_INTERVAL', 600)
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        while self.running:
            self.ping_domains()
            time.sleep(self.interval)

    def ping_domains(self):
        domains = Domain.objects.all()

        if len(domains) > 1:
            threads = []

            for domain in domains:
                thread = threading.Thread(target=self.ping_domain, args=(domain,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
        elif len(domains) == 1:
            self.ping_domain(domains[0])

    def ping_domain(self, domain):
        try:
            # Making a GET request to the domain and measuring the response time
            start_time = time.time()
            requests.get("https://" + domain.name)
            end_time = time.time()

            # Calculate the response time in milliseconds
            response_time = (end_time - start_time) * 1000

            # Saving response time in the database
            response_obj = ResponseTime(domain=domain, time=datetime.now(), response_time=response_time)
            response_obj.save()

            # Write log to stdout
            logger.info(f"Ping result for domain {domain.name}: {response_time}ms")
        except Exception as e:
            logger.error(f"Error pinging domain {domain.name}: {str(e)}")
