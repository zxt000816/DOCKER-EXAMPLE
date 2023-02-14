Create image:
     docker build -t zyf0706/cv-pytorch:0.0.3 .

Pull image:
     docker tag <image name> <user name>/<image name>:<version>        

Run in GPU:
    docker run --rm --gpus all -v C:\Users\zyf13\Desktop\test\DOCKER-EXAMPLE\code:/app zyf0706/cv-pytorch:0.0.3 python /app/main.py

Run in CPU:
    docker run --rm -v C:\Users\zyf13\Desktop\test\DOCKER-EXAMPLE\code:/app zyf0706/cv-pytorch:0.0.3 python /app/main.py

Work with Jupyter Notebook:
    docker run -p 8888:8888 -v C:\Users\zyf13\Desktop\test\DOCKER-EXAMPLE\code:/app zyf0706/cv-pytorch:0.0.3