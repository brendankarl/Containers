# Containers #
Some sample Containers that I've created whilst learning Docker and Python (a perfect combination!)

- **WorkoutGenerator** - Creates a workout with 8 random exercises (from a list of 26).
- **WorkoutGenerator - Docker Compose** - Uses Docker Compose to create two containers: Web (Flask) and DB (MySQL). A list of exercises is stored in the *exercises* database hosted on DB, which are returned by Web when browsing to http://127.0.0.1 or http://localhost on the host machine. To run these containers, all you need to do is to copy the *Workout Generator - Docker Compose* folder locally and execute `docker-compose up` from a terminal within the directory.
