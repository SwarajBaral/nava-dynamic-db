# How to Start the Server

To start the server, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/org_dynamic_db.git
    cd org_dynamic_db
    ```

2. **Set up environment variables**:
    Create a `.env` file in the root directory and add the necessary environment variables. For example:
        ```env
        MASTER_DB_URL=postgresql+asyncpg://admin:adminpass@db:5432/master_db
        DB_HOST=db
        DB_USER=admin
        DB_PASSWORD=adminpass
        POSTGRES_USER=admin
        POSTGRES_PASSWORD=adminpass
        POSTGRES_DB=master_db
        POSTGRES_PORT=5432
        ```

3. **Start the server using Docker Compose**:
    ```sh
    docker-compose up --build
    ```

4. **Access the server**:
    Open your browser and go to `http://localhost:6800`.

5. **Docs**:
    Docs for the server lives on `/docs`