# Flask Demo

## Local Development
1.  Install [pipenv](https://pipenv.pypa.io/en/latest/)
    ```shell
    pip3 install pipenv
    ```
2.  Install dependencies using pipenv
    ```shell
    pipenv install
    ```
3.  Create .env file (copy variables from .env.example).

4.  Run latest migrations
    ```
    pipenv run migrate
    ```
5.  Run the application
    ```shell
    pipenv run dev
    ```
## VSCode Setup
###  Set working pipenv python interpreter
1.  Open VSCode Command Palette by pressing ```Ctrl+Shift+P```
2.  Search and select ```Python: Select Interpreter```
3.  Select the path of your current pipenv install location
