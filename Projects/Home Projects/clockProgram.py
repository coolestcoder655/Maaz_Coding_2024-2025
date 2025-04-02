from datetime import time
import time as stopwatch

class Clock():
    def __init__(self, isStopwatch: bool = False, isTimer: bool = False):
        self.isStopwatch = isStopwatch
        self.isTimer = isTimer

        if self.isStopwatch == True and self.isTimer == True:
            self.isStopwatch, self.isTimer = False, False
            raise Exception("Cannot Have Both A Stopwatch and A Timer.")

    def switchMode(self, mode: str = "C"):
        mode = mode.upper()
        match mode:
            case "C":
                self.isStopwatch = False
                self.isTimer = False
            case "S":
                self.isStopwatch = True
                self.isTimer = False
            case "T":
                self.isStopwatch = False
                self.isTimer = False
            case _:
                raise Exception("No Mode Recognized, Can't Switch Mode")

    def getTime(self):
        if self.isStopwatch:
            raise Exception("Is A Stopwatch, Can't Get Time.")
        else:
            return time.strftime("%H:%M:%S", time.localtime())
        
    def startStopWatch(self):
        if not self.isStopwatch:
            raise Exception("Not A Stopwatch, Can't Start Watch.")
        else:
            self.stopWatchTime = stopwatch.time()

    def stopStopWatch(self):
        if self.isStopwatch:
            raise Exception("Is A Stopwatch, Can't Get Time.")
        elif self.startStopWatch == None:
            raise Exception("No Start Time, Can't Stop Watch")
        else:
            return float(time.time() - self.stopWatchTime)