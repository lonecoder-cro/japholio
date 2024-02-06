#!/usr/bin/env python3

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=1998)
