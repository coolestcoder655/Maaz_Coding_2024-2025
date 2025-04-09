class User:

    def __init__(self, name: str, weightLog: list[float], workoutSessions: list[dict]):
        self.name = name
        self.weightLog = weightLog
        self.workoutSessions = workoutSessions

    # Add Methods

    def addWeight(self, newWeight: float) -> None:
        self.weightLog.append(newWeight)

    def addWorkout(self, typeOfWorkout: str, duration: float, calories: int) -> None:
        # Store workouts in a consistent, simpler format
        self.workoutSessions.append({"type": typeOfWorkout, "duration": duration, "calories": calories})

    # Get/View Methods

    def getAverageCalories(self) -> (int, float):
        if len(self.workoutSessions) == 0:
            raise Exception("No workout sessions found. Please add.")

        calories = sum([x["calories"] for x in self.workoutSessions])
        return calories / len(self.workoutSessions)

    def weightChange(self) -> float:
        if len(self.weightLog) == 0:
            raise Exception("No weights found. Please add.")

        return self.weightLog[0] - self.weightLog[-1]

    def caloriesByType(self, workOutType: str) -> int:
        if len(self.workoutSessions) == 0:
            raise Exception("No workout sessions found. Please add.")

        calories = [
            workout["calories"] for workout in self.workoutSessions if workout["type"] == workOutType
        ]
        return sum(calories)

    def mostFrequentWorkout(self) -> str:
        if len(self.workoutSessions) == 0:
            raise Exception("No workout sessions found. Please add.")

        workout_counts = {}
        for workout in self.workoutSessions:
            workout_type = workout["type"]
            workout_counts[workout_type] = workout_counts.get(workout_type, 0) + 1

        return max(workout_counts, key=workout_counts.get).capitalize()

    def generateProgressReport(self) -> None:
        if len(self.weightLog) == 0:
            raise Exception("No weight logs found. Please add.")

        print(f"Name: {self.name}")
        print(f"Total Workouts: {len(self.workoutSessions)} Workouts")
        print(f"Total Calories: {sum([x['calories'] for x in self.workoutSessions])} Calories")
        print(f"Average Calories: {round(self.getAverageCalories(), 2)} Calories")
        print(f"Weight Change: {round(self.weightChange(), 2)} Pounds Difference")
        print(f"Most Frequent Workout: {self.mostFrequentWorkout()}")


# Example usage
user1 = User("Maaz", [], [])
user1.addWeight(72.5)
user1.addWeight(71.2)
user1.addWorkout("Running", 30, 280)
user1.addWorkout("Yoga", 60, 200)
user1.addWorkout("Running", 20, 180)
user1.generateProgressReport()