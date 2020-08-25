# Simple Python Flask service

- Build the image using the following command:

    ```bash
    docker build -t simple-flask:latest .
    ```

- Run the Docker container using the command shown below.

    ```bash
    docker run -d -p 5000:5000 simple-flask
    ```

- Access to the service:

    ```bash
    curl http://127.0.0.1:5000
    ```
