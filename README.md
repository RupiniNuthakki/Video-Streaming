# Video-Streaming
The project is a video streaming optimization service developed using Java and Python. It includes backend algorithms to enhance video delivery and playback, ensuring low latency and high availability. The service is deployed on AWS using Docker for containerization and Kubernetes for orchestration, achieving a 99.9% uptime.


1. Example videos are placed in videos directory like Nature.mp4, Tech.mp4.
2. Then python code is in app.py file.
3. Create a Dockerfile where code is written to build images in Docker.
4. Run python application on http://127.0.0.1:5000/-  gives welcome message
http://127.0.0.1:5000/video/Nature.mp4 - gives videos in server.
5. Used Kubernetes for orchestration and Afinally AWS for cloud deployment
