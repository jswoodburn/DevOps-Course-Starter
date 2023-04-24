## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

## Secrets/Environment variables

The To Do app runs off the back of the Trello API. To run the app locally you'll need to modify the values under `# Trello` in the `.env` file. If you have any issues with the below, check out the [`Trello API introduction docs`](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

***Remember to ensure that your .env file is listed in your .gitignore - never commit your API key or token to GitHub***

#### TRELLO_API_KEY

You can grab this from [`https://trello.com/app-key`](https://trello.com/app-key) if you're logged in to Trello. It should be at the top of the page as it loads, labelled `Key`.

#### TRELLO_API_TOKEN

On the same page where you found your API key - [`https://trello.com/app-key`](https://trello.com/app-key) - click the hyperlinked "Token" under the API key. Follow the instructions to grant permission to Server Token and get your token.

#### TRELLO_BOARD_ID

On your Trello homepage, i.e. `trello.com/<username>/boards`, navigate to the board you want to edit in the app. Then add `.json` to the url. 

>For example: 
>
>`https://trello.com/b/8AAcIEx2/devops-to-do-board` > `https://trello.com/b/8AAcIEx2/devops-to-do-board.json`.

Grab the value of `"id"` in the json that loads. This is the ID of your Trello board.

If you prefer you can also access this json/the ID by using the REST API itself (see the [Board API docs](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-memberships-get)).

## Running the App Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests

Tests can be found in the ```tests/``` directory. To run these tests from the terminal:
* Make sure you have pytest installed - if you have run ```poetry install``` then you should already have it as it's a dependency of the project.
* If you don't think you have pytest installed try running ```poetry add pytest --dev``` from the terminal
* Now to run the tests, you can stay in the terminal, navigate to the project root, and run ```poetry run pytest tests```. Here ```tests``` refers to the tests directory mentioned above, where all our tests are kept.
* If you want to run just one file of tests, you can be more specific: ```poetry run pytest tests/test_board.py```

If you want to add tests, be sure to conform to pytest standards and add them in a file that starts with ```test_``` or ends with ```_test``` and name any test function as ```test_<test_name>```.

## Running the App on a Virtual Machine

To run the app on a virtual machine(s):

1. Update the `todo_inventory` file to contain a list of the IP's of the virtual machines you want to run the app on.

2. Copy the files in the `ansible` directory to your control node. For example, using:

```bash
$ scp -r <relative_path_to_repo>/ansible/* <user>@<IP>:/home/<user>
```

3. Then ssh into that control node machine:

```bash
$ ssh <user>@<IP>
```

4. From here you should see all the files you've just copied across. You can run the app on all control nodes by running:

```bash
$ ansible-playbook todo_playbook.yml -i todo_inventory
```

5. You can check the app is running by visiting `http://<host-VM-IP>:5000` in a browser, replacing the <> section with each host IP address that you want to QC.

## Running the app in a Docker container

The app is set up to run in docker in development or production. You can also create an image to run the tests. In all the cases below `-it` can be replaced with `d` to run in detached mode.
 
### Development

Run:

    docker build --target development --tag todo-app:dev .

Then:

    docker run -it --env-file .env --publish 8081:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/todo-app/todo_app todo-app:dev

### Production

Run:

    docker build --target production --tag todo-app:prod .

Then:

    docker run -it --env-file .env --publish 8081:8088 todo-app:prod

### Tests

Run:

    docker build --target tests --tag todo-app:test .

Then:

    docker run -it todo-app:test


## Deploying production Docker image

The Docker image produced by the `publish-docker-image.yml` file can be found [here](https://hub.docker.com/r/jackiew104/todo-app). This is the same image used in the Azure Web App.

When the container image has a new version, you can prompt the app to pull it and restart by following the steps below:
1. In the [Azure Portal](https://portal.azure.com/) navigate to the Deployment Center of the To Do Web App (<Resource Group> | <App Service> | Deployment Center).
2. Copy the `Webhook URL`.
3. In a terminal, run the command below, ensuring that you first _escape the `$` in the webhook_ using a backslash.
    ```
    curl -dH -X POST "<webhook>"
    ```

## Live site

The site is hosted on Azure, and should be updated/redeployed when changes are pushed to `master`. The site can be found [here](https://jsw-todo-app.azurewebsites.net/).