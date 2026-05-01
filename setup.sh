#!/bin/bash
# =============================================
# Team Task Manager - One-Click Setup Script
# Run: chmod +x setup.sh && ./setup.sh
# =============================================

echo "=== Team Task Manager Setup ==="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt update && sudo apt install python3 python3-pip python3-venv -y
fi

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --quiet -r requirements.txt

# Set up .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    # Generate a secret key
    SECRET=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
    sed -i "s/your-very-secret-key-change-this/$SECRET/" .env
    echo ".env file created with auto-generated secret key."
fi

# Run migrations
echo "Running migrations..."
python3 manage.py migrate --no-input

# Collect static
echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To create an admin user run:"
echo "  source venv/bin/activate"
echo "  python3 manage.py createsuperuser"
echo ""
echo "To start the server run:"
echo "  source venv/bin/activate"
echo "  python3 manage.py runserver"
echo ""
echo "Then visit: http://localhost:8000/"
