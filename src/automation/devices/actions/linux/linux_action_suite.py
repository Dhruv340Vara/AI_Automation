from automation.devices.actions.device_action_registry import (DeviceActionRegistry,)
from automation.devices.actions.linux import (LinuxAppAction,LinuxShellAction,LinuxFileAction,)

class LinuxActionSuite:
    def __init__(self):
        self.registry = DeviceActionRegistry()
        self._register_actions()

    def _register_actions(self):
        self.registry.register(LinuxAppAction(),)
        self.registry.register(LinuxShellAction(),)
        self.registry.register(LinuxFileAction(),)

    def get_registry(self):
        return self.registry

    def list_actions(self):
        return list(self.registry._actions.keys())

    def __repr__(self):
        return (f"<LinuxActionSuite actions={len(self.registry)}>")
