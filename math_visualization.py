# math visualization assignment
# student score and function plots

import numpy as np
import matplotlib.pyplot as plt


# =========================
# part 1: mathematical function visualization
# =========================

x = np.linspace(-10, 10, 300)

y1 = x
y2 = x ** 2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="y = x", linestyle="-")
plt.plot(x, y2, label="y = x^2", linestyle="--")
plt.plot(x, y3, label="y = sin(x)", linestyle=":")
plt.plot(x, y4, label="y = e^(-0.1x) * cos(x)", linestyle="-.")

plt.title("mathematical function visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("function_plot.png", dpi=300, bbox_inches="tight")
plt.show()


# =========================
# part 2: my own equation
# =========================

x = np.linspace(-10, 10, 400)

# this equation mixes a cubic function with a trigonometric function
y = 0.02 * x ** 3 - 0.3 * x + 2 * np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="y = 0.02x^3 - 0.3x + 2sin(x)")

plt.title("my own equation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("own_equation.png", dpi=300, bbox_inches="tight")
plt.show()


# =========================
# part 3: student score data visualization
# =========================

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])

total = 0.4 * midterm + 0.6 * final

plt.figure(figsize=(8, 6))
plt.scatter(midterm, final)
plt.title("midterm score and final score")
plt.xlabel("midterm score")
plt.ylabel("final score")
plt.grid(True)
plt.savefig("score_scatter.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(total, bins=5, edgecolor="black")
plt.title("distribution of total scores")
plt.xlabel("total score")
plt.ylabel("number of students")
plt.grid(True)
plt.savefig("score_histogram.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(students, total)
plt.title("total score of each student")
plt.xlabel("student")
plt.ylabel("total score")
plt.grid(True, axis="y")
plt.savefig("score_bar_chart.png", dpi=300, bbox_inches="tight")
plt.show()


# =========================
# part 4: best-fit line and simple prediction
# =========================

slope, intercept = np.polyfit(midterm, final, 1)

prediction_x = np.linspace(50, 100, 100)
prediction_y = slope * prediction_x + intercept

plt.figure(figsize=(8, 6))
plt.scatter(midterm, final, label="original data")
plt.plot(prediction_x, prediction_y, label="best-fit prediction line")

plt.title("final score prediction from midterm score")
plt.xlabel("midterm score")
plt.ylabel("final score")
plt.legend()
plt.grid(True)
plt.savefig("score_prediction.png", dpi=300, bbox_inches="tight")
plt.show()

for score in [50, 75, 100]:
    predicted_final = slope * score + intercept
    print(f"predicted final score for midterm = {score}: {predicted_final:.2f}")
