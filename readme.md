# Project Three: Game Selection
By Levi and Isaac

Game Selection is a lightweight Python script to allow users to play multiple games, such as:

	• High/Low Game
	• RPS (Rock Paper Scissors)
	• Blackjack
	• Hangman
	• Slot Machine
	• Tic-Tac-Toe
	• Dice Game
	• AI Trivia (Requires OpenAI api access)
	• Clock Hand Angle Calculator (Not a game)
	• A Secret Game (Only accessible via special conditions) 




## Installation:


Requirements:

	• Python 3.9+
	• git (recommended for cloning the repository)
		• Other options include curl and wget, both work for all mainstream OSes
	• pip
	• OpenAI Python library (If you follow instructions it will be added during the install)
	• python-dotenv (If you follow instructions it will be added during the install)
	• OpenAI compatible API key, endpoint and model (MUST BE OPENAI library compatible!)

### Get the repo using git:

Using ```git clone```:
> Make sure git is installed if you want to use it

> If you don't have git, [the installation instructions are here](https://github.com/git-guides/install-git).
```
git clone https://github.com/100033398/Game-Selection.git
cd Game-Selection
```

Using ```curl```:
```
curl -L -o Game-Selection-main.zip https://github.com/100033398/Game-Selection/archive/refs/heads/main.zip
unzip Game-Selection-main.zip
cd Game-Selection-main
```

Using ```wget```:
```
wget -O Game-Selection-main.zip https://github.com/100033398/Game-Selection/archive/refs/heads/main.zip
unzip Game-Selection-main.zip
cd Game-Selection-main
```

### Set up a venv:

macOS/Linux:
```zsh
python3 -m venv .gamevenv
source .gamevenv/bin/activate
```

Windows:
```powershell
py -m venv .gamevenv
.\\.gamevenv\\Scripts\\Activate.ps1
```

### Installing all dependencies:
```
pip install -r requirements.txt
```


### Copy the .env:

macOS/Linux:
```zsh
cp .env.example .env
```

Windows:
```powershell
Copy-Item .env.example .env
```

### Set up the .env file for proper use of AI features:
> We recommend using nano or some other cli text editor, but any text editor works, such as VS code.

```
AI_API_KEY=your_api_key_here                  # your OpenAI-compatible API key
AI_ENDPOINT=https://api.openai.com/v1         # or your OpenAI-compatible endpoint
MODEL=ai_model_here                           # or another OpenAI-compatible model
```

### To edit the .env file ensuring proper use of AI features:

macOS/Linux:
```zsh
nano .env
```

Windows
```powershell
notepad .env
```

## Running:
> While in the python environment and folder called 'Game-Selection'

macOS/Linux (python3):
> Generally what is installed on modern systems
```zsh
python3 project_three.py
```

macOS/Linux (python):
```zsh
python project_three.py
```

Windows (py launcher):
```powershell
py project_three.py
```
