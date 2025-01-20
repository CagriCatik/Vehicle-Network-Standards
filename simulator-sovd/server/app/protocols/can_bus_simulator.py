import threading
import time
import random
import logging

logger = logging.getLogger('sovd_server')

class CANBusSimulator:
    def __init__(self, components, update_interval=1):
        """
        Simulates CAN bus messages for components.
        :param components: Dictionary of components
        :param update_interval: Time in seconds between CAN messages
        """
        self.components = components
        self.update_interval = update_interval
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run)
    
    def start(self):
        logger.info("Starting CAN Bus Simulator.")
        self.thread.start()
    
    def run(self):
        while not self._stop_event.is_set():
            for component in self.components.values():
                if component.id == "engine":
                    can_message = {
                        "id": "0x100",
                        "data": {
                            "rpm": component.data['rpm'],
                            "temperature": component.data['temperature']
                        }
                    }
                elif component.id == "transmission":
                    can_message = {
                        "id": "0x200",
                        "data": {
                            "gear": component.data['gear'],
                            "fluid_level": component.data['fluid_level']
                        }
                    }
                elif component.id == "door":
                    can_message = {
                        "id": "0x300",
                        "data": {
                            "status": component.data['status']
                        }
                    }
                else:
                    continue  # Unknown component
                
                # Simulate sending CAN message
                logger.debug(f"Sending CAN Message: {can_message}")
            time.sleep(self.update_interval)
    
    def stop(self):
        logger.info("Stopping CAN Bus Simulator.")
        self._stop_event.set()
        self.thread.join()
