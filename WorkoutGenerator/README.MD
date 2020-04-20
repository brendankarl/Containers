# Workout Generator #

This container runs Ubuntu and uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) to host a super-simple Python web application that generates a list of 8 random exercises (from a list of 26).

To run this container you will need [Docker](https://www.docker.com/) installed.

To get started copy the **WorkoutGenerator** folder locally and then run the following Docker commands from within the WorkoutGenerator directory, this will run the Container locally, listening on port 80 for requests. WorkoutGenerator can be accessed via http://localhost or http://127.0.0.1.

- `docker build -t workoutgenerator ./`

- `docker run -d -p 80:80 workoutgenerator`

Here is this super-advanced web app in action!

![Workout Generator in Action!](https://raw.githubusercontent.com/brendankarl/Containers/master/WorkoutGenerator/WorkoutGenerator.png)