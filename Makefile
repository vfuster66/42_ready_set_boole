IMAGE_NAME = enter-the-matrix

build:
	docker build -t $(IMAGE_NAME) .

test: 
	docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) python tests/test_$(EX).py

test_all:
	docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) python -m unittest discover -s tests -p "test_*.py" --top-level-directory .

clean:
	docker system prune -f

purge:
	docker rmi $(IMAGE_NAME)