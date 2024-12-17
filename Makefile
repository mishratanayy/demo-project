setup:
	@echo "Creating virtual environment and activating it"
	python3 -m venv venv && source venv/bin/activate

install:
	@echo "Making sure venv exists"
	$(MAKE) setup
	@echo "Installing required packages"
	pip3 install -r requirements.txt

run:
	$(MAKE) install
	@echo "Running server"
	python3 run.py

clean:
	@echo "Deactivating and deleting virtual environment"
	ifeq ($(wildcard $(venv)),)
		deactivate
		rm -rf venv
	endif