MONGO_CONTAINER_NAME=ib-mongo
MONGO_URI=mongodb://localhost:27020/db
TEST_MONGO_URI=mongodb://localhost:27020/test_db

deps:
	pip install -r requirements.txt

init_venv:
	python3 -m venv env

activate_venv:
	. env/bin/activate

deactivate_env:
	deactivate

run_local:
	$(MAKE) activate_venv
	MONGO_URI=$(MONGO_URI) python wsgi.py

run_mongo:
	@echo "Starting mongo container..."
	docker run --rm --name $(MONGO_CONTAINER_NAME) -p 27020:27017 -d mongo

rm_mongo:
	@echo "Purging mongo container..."
	-docker kill $(MONGO_CONTAINER_NAME)

run_tests:
	TEST_MONGO_URI=$(TEST_MONGO_URI) pytest -v -s