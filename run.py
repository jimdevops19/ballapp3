from ballapp3 import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=True,
        host="10.100.102.12",
        port="5001"
    )