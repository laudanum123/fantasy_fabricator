#!/bin/bash
# Start the server
python backend/app.py &
cd frontend 
npm run serve