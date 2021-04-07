from app.factory import create_flask

if __name__ == "__main__":
    app = create_flask(test=False)
    app.run(debug=True, host="0.0.0.0")