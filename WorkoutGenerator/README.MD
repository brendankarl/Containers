# Workout Generator #

This container runs Ubuntu and uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) to host a super-simple Python web application that generates a list of 8 random exercises (from a list of 26).

To run this container you will need [Docker](https://www.docker.com/) installed.

To run this sample you'll need to copy the **WorkoutGenerator** folder and then run the following Docker commands from within the WorkoutGenerator directory, this will run the Container locally, listening on port 80 for requests. WorkoutGenerator can be accessed via http://localhost:80.

-`docker build -t workoutgenerator ./`

-`docker run -d -p 80:80 workoutgenerator`