import matplotlib.pyplot as plt
import numpy as np

class User:

    def __init__(self, name: str, weightLog: list[float] = list(), workoutSessions: list[dict] = list()):
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

    def getAverageCalories(self) -> int | float:
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

    def plotGraph(self):
        if len(self.weightLog) == 0:
            raise Exception("No Weight To Plot.")
        # Months = X
        # Weights = Y
        
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        weights = list()
        yPositions = list()
        offset = -2.5

        for weight in self.weightLog:
            weights.append(weight)
            yPositions.append(weight + offset)

        _, ax = plt.subplots()
        ax.plot(months[0 : len(weights)], weights, linestyle="dashed", color="red", marker="o", linewidth=2)
        ax.set_xlabel(r'$\bf{Time}$ $\it{(Months)}$', fontsize=16)
        ax.set_ylabel(r'$\bf{Weight}$ $\it{(Kilograms)}$', fontsize=16)
        
        for weight in weights:
            ax.text(months[yPositions.index(weight + offset)], yPositions[weights.index(weight)], f"{round(weights[weights.index(weight) - 1] - weight, 2)})", fontsize=10)
        ax.set_title("Weight Change over Months")


        plt.tight_layout()
        plt.grid()
        plt.show()