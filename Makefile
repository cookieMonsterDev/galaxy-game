init:
		pip3 install -r requirements.txt

start:
		python3 src/main.py

build:
		pyinstaller --onefile --windowed --name=tic-tac-toe src/main.py

