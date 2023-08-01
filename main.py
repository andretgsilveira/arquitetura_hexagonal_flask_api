from services.adapters.primary import create_flask_app


if __name__ == '__main__':
    app = create_flask_app()
    app.run(debug=True, host='0.0.0.0')