import threading
import time
import random
import logging

logger = logging.getLogger('sovd_server')

class RealTimeSimulator:
    def __init__(self, components, update_interval=5):
        """
        :param components: Dictionary of components to simulate
        :param update_interval: Time in seconds between updates
        """
        self.components = components
        self.update_interval = update_interval
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run)
    
    def start(self):
        logger.info("Starting Real-Time Data Simulator.")
        self.thread.start()
    
    def run(self):
        while not self._stop_event.is_set():
            for component in self.components.values():
                if component.id == "engine":
                    # Simulate RPM and temperature fluctuations
                    component.data['rpm'] = max(600, min(3000, component.data['rpm'] + random.randint(-100, 100)))
                    component.data['temperature'] = max(70, min(120, component.data['temperature'] + random.randint(-5, 5)))
                elif component.id == "transmission":
                    # Simulate gear changes
                    possible_gears = ['P', 'R', 'N', 'D', '2', '1']
                    component.data['gear'] = random.choice(possible_gears)
                    # Simulate fluid level
                    component.data['fluid_level'] = random.choice(['Low', 'Medium', 'High'])
                elif component.id == "door":
                    # Simulate door status
                    component.data['status'] = random.choice(['open', 'closed'])
            time.sleep(self.update_interval)
    
    def stop(self):
        logger.info("Stopping Real-Time Data Simulator.")
        self._stop_event.set()
        self.thread.join()
