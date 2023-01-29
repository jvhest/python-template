#!/bin/sh
echo "🚀 Creating .env file for direnv utility"
echo "export VIRTUAL_ENV=$(poetry env info --path)" > .envrc
echo "export PATH=$(poetry env info --path)/bin:\$PATH" >> .envrc
