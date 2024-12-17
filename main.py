from app import run



app = run.create_app()

if __name__ == "__main__":
    app.run(debug = True)