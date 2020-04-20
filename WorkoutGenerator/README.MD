# Workout Generator #

This container runs Ubuntu and uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) to host a super-simple Python web application that generates a list of 8 random exercises (from a list of 26).

To run this container you will need [Docker](https://www.docker.com/) installed.

To get started copy the **WorkoutGenerator** folder locally and then run the following Docker commands from within the WorkoutGenerator directory, this will run the Container locally, listening on port 80 for requests. WorkoutGenerator can then be accessed via http://localhost or http://127.0.0.1.

- `docker build -t workoutgenerator ./`

- `docker run -d -p 80:80 workoutgenerator`

Here is this super-advanced web app in action!

![Workout Generator in Action!](https://raw.githubusercontent.com/brendankarl/Containers/master/WorkoutGenerator/WorkoutGenerator.png)

## Removing the Container ##
To remove the Container and Images created above run the following commands
- `docker ps` to list the running Containers, take a note of the "CONTAINER ID" for the workoutgenerator container
- `docker container stop (CONTAINER ID)` to stop the workoutgenerator Container
- `docker rm (CONTAINER ID)` to remove the workoutgenerator Container
- `docker rmi workoutgenerator` to remove the workoutgenerator Image
- `docker rmi ubuntu` to remove the Ubuntu Image used by workoutgenerator (don't run this if you have any images that depend on the Ubuntu container).