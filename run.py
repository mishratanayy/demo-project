from app import create_app

app = None

if __name__ == "__main__":
    if app == None:
        app = create_app()
    app.run(debug=True,port = 5004,host="0.0.0.0")