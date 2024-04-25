echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.9 version"
conda create --prefix ./.venv python=3.9 -y
echo [$(date)]: "activating the environment"
conda  activate ./.venv
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"