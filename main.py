from services.adapters.primary import create_flask_app
import logging

if __name__ == '__main__':

    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger("api")
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    app = create_flask_app(logger)
    app.run(debug=True, host='0.0.0.0')