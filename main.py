import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import sys

MAX_ITER = 5000  # Gradient descent iterations per restart
LEARNING_RATE = 0.01/(MAX_ITER)  # Don't touch
NUM_RESTARTS = 20  # Number of random starts for gradient descent
everyXthFrame = 100  # max_iter / this number = number of frames shown in animation
INITIALINTERVAL = 150  # Initial speed of animation (bigger is slower)
animation_direction = 1  # 1 for forward, -1 for backward
current_frame = 0  # Current frame index
is_paused = False

choice = "hi"
waitingForInput = True
while waitingForInput:
    print("\nChoose how to input points:")
    print("1. Random Points")
    print("2. Custom Points")
    print("3. Suggested Points")
    print("4. Quit")
    choice = input(">")
    try:
        assert 0 < int(choice) and int(choice) < 5
        waitingForInput = False
        choice = int(choice)
    except:
        pass

if choice == 1:
    numPoints = 0
    waitingForInput = True
    while waitingForInput:
        print("\nInput the number of points:")
        userIn = input(">")
        try:
            assert 1 < int(userIn)
            waitingForInput = False
            numPoints = int(userIn)
        except:
            print("Please request at least 2 points")

    points = np.random.rand(numPoints, 3) * 5

if choice == 2:
    numPoints = 0
    waitingForInput = True
    while waitingForInput:
        print("\nInput the number of points:")
        userIn = input(">")
        try:
            assert 1 < int(userIn)
            waitingForInput = False
            numPoints = int(userIn)
        except:
            print("Please input at least 2 points")

    points = []
    for i in range(numPoints):
        x, y, z = 0, 0, 0
        for coord, label in zip([x, y, z], ["x", "y", "z"]):
            waitingForInput = True
            while waitingForInput:
                print(f"\nInput the {label} coordinate for point number {i + 1}:")
                userIn = input(">")
                try:
                    coord = int(userIn)
                    waitingForInput = False
                except:
                    pass
        points.append([x, y, z])

    points = np.array(points)

if choice == 3:
    points = np.array([
        [1, 2, 1],
        [1, 2, 2],
        [3, 3, 3],
        [4, 4, 4],
        [5, 5, 5],
        [1, 1, 3],
        [2, 3, 3],
        [3, 5, 5],
        [4, 5, 7],
        [5, 6, 7]])
if choice == 4:
    sys.exit()

def projection_distance_to_plane(plane_params, point):
    a, b, c, d = plane_params
    x, y, z = point
    normal = np.array([a, b, c])
    point_vec = np.array([x, y, z])
    dot_product = np.dot(normal, point_vec) + d
    return (dot_product ** 2) / np.linalg.norm(normal) ** 2

def compute_gradient(plane_params, points):
    a, b, c, d = plane_params
    grad_a, grad_b, grad_c, grad_d = 0, 0, 0, 0
    for point in points:
        x, y, z = point
        normal = np.array([a, b, c])
        point_vec = np.array([x, y, z])
        dot_product = np.dot(normal, point_vec) + d
        norm_squared = np.linalg.norm(normal) ** 2
        grad_common = 2 * dot_product / norm_squared
        grad_a += grad_common * (x - dot_product * a / norm_squared)
        grad_b += grad_common * (y - dot_product * b / norm_squared)
        grad_c += grad_common * (z - dot_product * c / norm_squared)
        grad_d += grad_common
    return np.array([grad_a, grad_b, grad_c, grad_d])

def gradient_descent(points, max_iter=MAX_ITER, learning_rate=LEARNING_RATE):
    current_solution = (2 * np.random.rand(4)) - 1
    history = []
    for iter in range(max_iter + 1):
        gradient = compute_gradient(current_solution, points)
        current_solution -= learning_rate * gradient
        if (iter % everyXthFrame == 0):
            history.append(current_solution.copy())
    return history

def fit_plane_with_multiple_starts(points, n_restarts=NUM_RESTARTS):
    best_solution = None
    best_history = None
    lowest_error = np.inf
    for i in range(n_restarts):
        print(f"Restart {i + 1}/{n_restarts}...", end="\r")
        history = gradient_descent(points)
        final_plane = history[-1]
        total_error = np.sum([projection_distance_to_plane(final_plane, point) for point in points])
        if total_error < lowest_error:
            lowest_error = total_error
            best_solution = final_plane
            best_history = history
    print("\nComputation complete.")
    print("Error: " + str(lowest_error))
    print("Plane Equation: " + str(final_plane[0]) + "x + " + str(final_plane[1]) + "y + " + str(final_plane[2]) + "z + " + str(final_plane[3]) + " = 0")
    return best_solution, best_history

best_plane, best_history = fit_plane_with_multiple_starts(points)

# Animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update_ani_with_direction(frame):
    global current_frame
    current_frame += animation_direction
    if current_frame < 0:
        current_frame = 0
    elif current_frame >= len(best_history):
        current_frame = len(best_history) - 1
    update_ani(current_frame)

def update_ani(frame):
    ax.clear()
    plane_params = best_history[frame]
    a, b, c, d = plane_params
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r', label='Points')
    xx, yy = np.meshgrid(np.linspace(points[:, 0].min(), points[:, 0].max(), 20), np.linspace(points[:, 1].min(), points[:, 1].max(), 20))
    zz = (-a * xx - b * yy - d) / c
    ax.plot_surface(xx, yy, zz, alpha=0.3, color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Iteration: {(frame) * everyXthFrame}/{(len(best_history) - 1) * everyXthFrame}')
    ax.legend()

ani = FuncAnimation(fig, update_ani_with_direction, frames=len(best_history), interval=INITIALINTERVAL, repeat=True)

def reverse_animation(event):
    global animation_direction
    animation_direction *= -1  # Toggle animation direction

def toggle_pause(event):
    global is_paused
    if is_paused:
        is_paused = not is_paused
        ani.event_source.start()
        pause_button.label.set_text('Pause')
    else:
        ani.event_source.stop()
        is_paused = not is_paused
        update_ani(current_frame)
        pause_button.label.set_text('Play')

button_ax_reverse = plt.axes([0.8, 0.06, 0.15, 0.05])  # x, y, width, height
reverse_button = Button(button_ax_reverse, 'Reverse', color='lightgoldenrodyellow', hovercolor='lightcoral')
reverse_button.on_clicked(reverse_animation)

button_ax_pause = plt.axes([0.8, 0.0, 0.15, 0.05])  # x, y, width, height
pause_button = Button(button_ax_pause, 'Pause', color='lightgoldenrodyellow', hovercolor='lightcoral')
pause_button.on_clicked(toggle_pause)


plt.show()
