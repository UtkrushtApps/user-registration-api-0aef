# User Registration API with Unique Email Constraint

## Task Overview

You are building a user registration service for a growing SaaS platform that manages individual user accounts. The current system allows multiple registrations with the same email address, leading to duplicate user records, inconsistent authentication, and downstream issues in user management. To provide a reliable user experience and ensure data integrity, it's essential to enforce unique email constraints at both the API and database layers.

## Guidance

- The project is focused on designing a robust FastAPI backend for user registration, leveraging PostgreSQL for data persistence.
- Employ proper data validation for incoming user registration data, especially for email format and password fields.
- Ensure that the database schema enforces uniqueness on the email field to prevent accidental duplicates, regardless of the application logic.
- Use async SQLAlchemy for database interactions, and provide clear error messages and HTTP status codes when duplicate registration attempts occur.
- Follow best practices for organizing FastAPI applications, including modular routers, models, and service layers.

## Objectives

- Implement a user registration API endpoint that accepts email, full name, and password fields, validating input with Pydantic.
- Ensure the API and the PostgreSQL database enforce that each email can only be registered once.
- Handle duplicate registration attempts gracefully by returning a clear error message and appropriate HTTP status code.
- Provide an endpoint to list all registered users, returning their id, email, and full name.
- Use Docker and Docker Compose to containerize the FastAPI app alongside the PostgreSQL database.

## How to Verify

- Attempt to register a new user with a unique email and verify a successful response with the user's id, email, and full name.
- Attempt to register another user with the same email and confirm that the API returns an error message indicating the email is already registered, along with a suitable status code (e.g., 400 or 409).
- Use the users listing endpoint to ensure only unique user records exist in the database.
- Check that duplicate entries are not present in the database even after multiple duplicate registration attempts.
