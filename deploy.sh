# build our heroku-ready local Docker image
docker build -t cars -f Dockerfile .


# push your directory container for the web process to heroku
heroku container:push web -a guarded-ocean-69420


# promote the web process with your container
heroku container:release web -a guarded-ocean-69420


# run migrations
heroku run python3 manage.py migrate -a guarded-ocean-69420