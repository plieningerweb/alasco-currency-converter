"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set environment variables.
"""
import os

ENV = os.getenv("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")
