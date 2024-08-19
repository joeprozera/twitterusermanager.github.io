# Twitter user management
 # Twitter Username Manager  ## Description  This Flask application allows users to submit Twitter usernames through a web form. It checks if the username is already followed and stores new usernames in an SQLite database.  ## Features  - Submit Twitter usernames through a web form. - Check for duplicates before saving. - Simple and easy-to-use interface.  ## Getting Started  ### Prerequisites  - Python 3.8 or higher - Flask - Flask-SQLAlchemy  ### Installation  1. Clone the repository:      ```bash     git clone https://github.com/yourusername/twitter-username-manager.git     ```  2. Navigate to the project directory:      ```bash     cd twitter-username-manager     ```  3. Create a virtual environment and activate it:      ```bash     python -m venv venv     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`     ```  4. Install the required packages:      ```bash     pip install -r requirements.txt     ```  5. Run the application:      ```bash     python app.py     ```  ### Deployment  Deployed on Heroku. Access the app at [your-repl-url](https://your-app-name.herokuapp.com).  ## License  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
