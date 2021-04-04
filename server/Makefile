MONGO_CONTAINER_NAME=ib-mongo
MONGO_PORT=27020
MONGO_URI=mongodb://localhost:$(MONGO_PORT)/db
TEST_MONGO_URI=mongodb://localhost:$(MONGO_PORT)/test_db

deps:
	pip install -r requirements.txt

init_venv:
	python3 -m venv env

run_local:
	$(MAKE) activate_venv
	MONGO_URI=$(MONGO_URI) python wsgi.py

run_mongo:
	@echo "Starting mongo container..."
	docker run --rm --name $(MONGO_CONTAINER_NAME) -p $(MONGO_PORT):27017 -d mongo

rm_mongo:
	@echo "Purging mongo container..."
	-docker kill $(MONGO_CONTAINER_NAME)

run_tests:
	TEST_MONGO_URI=$(TEST_MONGO_URI) pytest -v -s