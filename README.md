# Car Wash Service Reservation System

This project is a web-based reservation system for car wash services. It allows customers to book appointments online and make payments securely through Stripe.

## Features

- User registration and authentication
- Book car wash services online
- Manage reservations
- Integration with Stripe for secure payments
- Admin panel for managing services and reservations

## Technologies Used

- Django
- PostgreSQL
- Stripe

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Marjol-Mata/carwash_service_reservation.git
    cd carwash_service_reservation
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Configuration

### Stripe Integration

To integrate Stripe, you need to set up the following environment variables:

- `STRIPE_SECRET_KEY`
- `STRIPE_PUBLISHABLE_KEY`
