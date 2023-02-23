# News Website

This is a simple news website created using Flask. The website fetches the latest news articles from the NDTV API and displays them on the homepage. The project is hosted on Vercel, a cloud platform for serverless deployment.

## Features

- Latest news articles displayed on the homepage
- Clicking on a news article takes the user to the full article on the NDTV website

## Technologies Used

- Python
- Flask
- HTML/CSS/JavaScript

## Hosted on Vercel

This project is hosted on Vercel, a cloud platform for serverless deployment. You can access the live website at https://news19.vercel.app/.

## API Used

This project fetches the latest news articles from the NDTV API, which can be found at https://ndtvapi.vercel.app/. The API provides news articles in JSON format.

## Getting Started

To run this project on your local machine, follow the steps below:

1. Clone the repository using the following command:
```bash
    $ git clone https://github.com/NishanthMuruganantham/news-website.git
```

2. Navigate to the cloned directory:
```bash
    $ cd news-website
```
3. Install the project dependencies:
```bash
    $ pip install -r requirements.txt
```
4. Set the Flask environment variables:
```bash
    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
```
5. Run the Flask app
```bash
    $ python app.py
```

6. Open a web browser and go to http://localhost:5000/ to access the website.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them with a descriptive commit message.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
