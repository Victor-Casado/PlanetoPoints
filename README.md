# Linear Algebra Semester 1 Reflection
## Overview
### Purpose

This program calculates the best-fitting plane for a set of 3D points using gradient descent. By minimizing the total squared distance between the points and the plane, it ensures an optimal fit. The program is interactive, letting you pick how to input points, runs multiple tries to get the best fit, and shows the process with a dynamic 3D animation.

### Key Features

#### Input Methods

* Random Points: The program makes random 3D points for you.

* Custom Points: You type in the coordinates for your own points.

* Suggested Points: The program gives you a pre-made set of points to use.

#### Gradient Descent Optimization

The program uses gradient descent to tweak the plane to minimize the total squared distance to the points. To improve accuracy, the program performs multiple random restarts, avoiding issues with local minima.

#### 3D Animation

The program visualizes the best run from all the restarts using a 3D animation. This animation shows the points and the plane as it evolves to minimize the total squared distance.

#### Libraries Used

* NumPy: Handles some of the math and stores the data.

* Matplotlib: Does the 3D visualization and animation.

* Matplotlib Widgets: Adds interactive buttons for pausing, playing, and reversing the animation.

## Install Guide:

**Cloning the Project**

1. In terminal, clone the repository to your local machine:

        git clone git@github.com:Victor-Casado/PlanetoPoints.git


**Installing Dependencies**

1. Navigate to [Python Download Page](https://www.python.org/downloads/) and install python3 on your machine

   **<ins>Note: The commands in this guide use python3 to refer to Python. Depending on your system, the command may be python or another variation.</ins>**
   
2. Create a virtual environment by running
 
        python3 -m venv foo

3. Activate the virtual environment

* On linux/mac (I believe but have not tested on mac):

        . foo/bin/activate

* On windows:

        . foo/Scripts/activate


5. In your terminal, run the command (where the -r is placed depends on system, but the terminal should tell you)

        pip install -r PlanetoPoints/requirements.txt
   
## Launch Codes

1. Activate the virtual environment from the install guide if not activated already

2. Run the App:

        $ python3 main.py

   
