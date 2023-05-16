docker build -t fast_api .
docker run -it --name fastapi -p 8082:8080  -d --rm fast_api
