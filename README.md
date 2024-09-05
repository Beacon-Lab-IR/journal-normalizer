# Journal Log Converter

This project provides tools to convert binary journal logs and hexadecimal logs into readable ASCII strings. The scripts are containerized using Docker, allowing you to run them on any platform that supports Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

## Project Structure

- `convert_hex.py`: A Python script that converts hexadecimal strings in logs to readable ASCII strings.
- `convert.py`: A script for converting binary journal logs.
- `Dockerfile`: A file to build the Docker image.

## Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:Beacon-Lab-IR/journal-normalizer.git
   cd journal-normalizer
   ```

1. **Build the Docker image**:

    ```bash
    docker build -t journal_normalizer:latest .
    ```
## Usage
### Converting Binary Journal Logs
To convert binary journal logs to strings, place your journal files in a local directory (e.g., logs/), and run:
 ```bash
docker run --rm -v "$(pwd)/logs:/logs" journal_normalizer:latest
```
It will create a .txt files with the same name of the original journals files (with different extension).

### Converting HEX to Strings 
To convert hexadecimal logs, use the following command:
 ```bash
docker run --rm -v "$(pwd)/logs:/logs" journal_normalizer:latest python3 /code/hex_to_string.py /logs/input_log.txt /logs/converted_output.txt
```

## Test

TODO

