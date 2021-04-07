# Flask Server

### Make sure you have the `creds.json` file for GCP APIs

-   Obtain `creds.json` file on request
-   Place file as `creds.json` under the `server` folder
-   Set the `GOOGLE_APPLICATION_CREDENTIALS` env var to the **absolute** path of the `creds.json` file

```bash
$ cd server
$ export GOOGLE_APPLICATION_CREDENTIALS="$PWD/creds.json"
```

### Run locally

To run the flask server and celery worker locally, use the `Makefile` in the `server` folder. Make sure that the `GOOGLE_APPLICATION_CREDENTIALS` env var is set.
<br>
<br>
Bash Commands: (Tested on Ubuntu 20.04)

```bash
# terminal window 1
$ make init_venv        # Only needed first time, create python virtual env
$ . env/bin/activate    # Activate python virtual env
$ make deps             # First time and as needed, install pip packages
$ make run_flask        # Provision mongo and redis containers and then run flask app

# terminal window 2
$ . env/bin/activate    # Activate python virtual env
$ make run_local        # Run the worker
```

To run tests using `pytest`

```bash
# Make sure to activate virtual env (create if needed),
# install all packages and run the mongo container
$ make run_tests
```
