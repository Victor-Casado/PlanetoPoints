# Linear Algebra Semester 1 Reflection
## Overview
### Purpose

This program helps find the best-fitting plane for a  3D points using gradient descent. It tries to make the plane as close as possible to all the points by minimizing the total squared distance. The program is interactive, letting you pick how to input points, runs multiple tries to get the best fit, and shows the process with a cool 3D animation.

### Key Features

1. Input Methods

You can pick one of three ways to define your points:

* Random Points: The program makes a bunch of random 3D points for you.

* Custom Points: You type in the coordinates for your own points.

* Suggested Points: The program gives you a pre-made set of points to use.

2. Gradient Descent Optimization

The program uses gradient descent to tweak the plane step by step until it fits the points as well as possible.

It also runs multiple random restarts so it doesn’t get stuck in local minima.

For best results, you may want to tweak the values at the top of the program.

3. 3D Animation

The best run out of all the restarts is animated in 3D so you can watch the plane "learn" to fit the points:

The points and the evolving plane are shown live.

You can control the speed and direction of the animation.

Buttons let you pause, play, and reverse the animation.

4. Interactivity

You get to control the program in two ways:

Through the command line, where you choose how to input points and set options.

Through buttons in the animation window to adjust how it plays out.

Libraries Used

NumPy: Handles some of the math and stores the data.

Matplotlib: Does the 3D visualization and animation.

Matplotlib Widgets: Adds interactive buttons for pausing, playing, and reversing the animation.

## Install Guide:

**Cloning the Project**

1. In terminal, clone the repository to your local machine:

        git clone git@github.com:Victor-Casado/PlanetoPoints.git


**Installing Dependencies**

1. Navigate to [Python Download Page](https://www.python.org/downloads/) and install python3 on your machine

   **<ins>Note: all python commands are denoted here as python3, but on your machine they may be python or something else</ins>**
   
2. Create a virtual environment by running
 
        python3 -m venv foo

3. Activate the virtual environment

   On linux/mac (I believe but have not tested on mac):

        . foo/bin/activate
   On windows:

        . foo/Scripts/activate


4. In your terminal, run the command (where the -r is placed depends on system, but the terminal should tell you)

        pip install -r PlanetoPoints/requirements.txt
   
## Launch Codes

1. Activate the virtual environment from the install guide if not activated already

2. Run the App:

        $ python3 main.py

   
