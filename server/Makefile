MONGO_CONTAINER_NAME=ib-mongo
MONGO_PORT=27020
MONGO_URI=mongodb://localhost:$(MONGO_PORT)/db

REDIS_CONTAINER_NAME=ib-redis
REDIS_PORT=6379
REDIS_URI=redis://localhost:$(REDIS_PORT)/0

TEST_MONGO_URI=mongodb://localhost:$(MONGO_PORT)/test_db


deps:
	pip install -r requirements.txt

init_venv:
	python3 -m venv env

run_mongo:
	$(MAKE) rm_mongo
	@echo "Starting mongo container..."
	docker run --rm --name $(MONGO_CONTAINER_NAME) -p $(MONGO_PORT):27017 -d mongo

rm_mongo:
	@echo "Purging mongo container..."
	-docker kill $(MONGO_CONTAINER_NAME)

run_redis:
	$(MAKE) rm_redis
	@echo "Starting redis container..."
	docker run --rm --name $(REDIS_CONTAINER_NAME) -p $(REDIS_PORT):6379 -d redis

rm_redis:
	@echo "Purging redis container..."
	-docker kill $(REDIS_CONTAINER_NAME)

run_flask:
	$(MAKE) run_mongo
	$(MAKE) run_redis
	MONGO_URI=$(MONGO_URI) REDIS_URI=$(REDIS_URI) python wsgi.py

run_worker:
	MONGO_URI=$(MONGO_URI) REDIS_URI=$(REDIS_URI) celery -A worker.celery worker -l INFO

run_tests:
	$(MAKE) run_mongo
	$(MAKE) run_redis
	REDIS_URI=$(REDIS_URI) TEST_MONGO_URI=$(TEST_MONGO_URI) pytest -rA -v -s
	$(MAKE) rm_mongo
	$(MAKE) rm_redis