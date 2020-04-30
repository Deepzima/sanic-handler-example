# Environment Tasks
ENV_PATH = $(wildcard ./venv)

env-inst: 
	@echo "Start Environment"
	./scripts/venvinstall.sh

env-activ:
	@echo "Virtualenv Activate"
	source ./venv/bin/activate

env-deact:
	@echo "Virtualenv Deactivate"
	deactivate
