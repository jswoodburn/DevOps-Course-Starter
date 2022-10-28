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