IMAGE_NAME = enter-the-matrix

build:
	docker build -t $(IMAGE_NAME) .

# ➤ Clean & Purge
clean:
	docker system prune -f

purge:
	docker rmi $(IMAGE_NAME)

# ➤ Global Tests
test_all:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest tests/

# ➤ Ex00
run_ex00:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex00/tester.py

test_ex00:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_00.py

# ➤ Ex01
run_ex01:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex01/tester.py

test_ex01:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_01.py

# ➤ Ex02
run_ex02:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex02/tester.py

test_ex02:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_02.py

# ➤ Ex03
run_ex03:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex03/tester.py

test_ex03:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_03.py

# ➤ Ex04
run_ex04:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex04/tester.py

test_ex04:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_04.py

# ➤ Ex05
run_ex05:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex05/tester.py

test_ex05:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_05.py

# ➤ Ex06
run_ex06:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex06/tester.py

test_ex06:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_06.py

# ➤ Ex07
run_ex07:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex07/tester.py

test_ex07:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_07.py

# ➤ Ex08
run_ex08:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex08/tester.py

test_ex08:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_08.py

# ➤ Ex09
run_ex09:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex09/tester.py

test_ex09:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_09.py

# ➤ Ex10
run_ex10:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex10/tester.py

test_ex10:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_10.py

# ➤ Ex11
run_ex11:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	python ex11/tester.py

test_ex11:
	@docker run --rm -it -v $(PWD):/app -w /app -e PYTHONPATH=/app $(IMAGE_NAME) \
	pytest -s tests/test_11.py
