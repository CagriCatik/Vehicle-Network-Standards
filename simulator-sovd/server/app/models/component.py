from dataclasses import dataclass, field
from typing import List, Dict
import uuid

@dataclass
class Fault:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    code: str
    description: str
    severity: str = "medium"  # 'low', 'medium', 'high'
    status: str = "open"      # 'open', 'cleared'

@dataclass
class Component:
    id: str
    name: str
    faults: List[Fault] = field(default_factory=list)
    data: Dict[str, any] = field(default_factory=dict)
    locked: bool = False
    lock_id: str = None

    def reset_faults(self):
        self.faults.clear()

    def clear_fault_code(self, fault_code: str) -> bool:
        initial_count = len(self.faults)
        self.faults = [fault for fault in self.faults if fault.code != fault_code]
        return len(self.faults) < initial_count

    def add_fault(self, code: str, description: str, severity: str = "medium"):
        self.faults.append(Fault(code=code, description=description, severity=severity))

    def lock_component(self, requester_id: str) -> bool:
        if not self.locked:
            self.locked = True
            self.lock_id = requester_id
            return True
        return False

    def unlock_component(self, requester_id: str) -> bool:
        if self.locked and self.lock_id == requester_id:
            self.locked = False
            self.lock_id = None
            return True
        return False
