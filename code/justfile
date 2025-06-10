# List all available commands
default:
    @just --list

# Install project dependencies
install:
    pip3 install -r requirements.txt


# Check code style (ignoring venv directory)
lint:
    flake8 . --exclude=venv/* --max-line-length=120

# Format code using black
format:
    black . --exclude=venv/* --line-length=120

push:
    git pull
    git add .
    git commit -m "Update $(date +%Y-%m-%d)"
    git push