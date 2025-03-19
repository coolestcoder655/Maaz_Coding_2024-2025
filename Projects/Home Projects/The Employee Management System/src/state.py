from enum import Enum

class State(Enum):
    Login = 0
    EmployeeMenu = 1
    ManagerMenu = 2
    CEOMenu = 3
    JanitorMenu = 4
    SecurityGuardMenu = 5
    ITSupportMenu = 6
    Lockdown = 7
    Exit = 8
    FloormartManagementMode = 9