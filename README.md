
# How to setup the AI and get it working!






## What you need

#### IDE & Python

Star with setting up your IDE of choice and python, I will cover how i've set it up in VSCode

#### Ollama

You need to have Ollama installed and the model Qwen2.5-Coder

You can install Ollam here : https://ollama.com/

#### Google Chrome

Due to a library i use that helps me scrabe websites, Google Chrome is needed to run the program, it will open a chrome window, so it needs Google Chrome and its driver installed (The driver comes with google chrome installation already)


## Installing Qwen in Ollama

After installing Ollama on your pc run this command in your terminal

```bash
  Ollama run Qwen2.5-Coder
```

## Setting up enviorment

Inside VSCode there is a search bar at the top in that type

```bash
  >Python 
```
and select "Create Python enviorment", once that is done run this in the terminal
```bash
  .venv/scripts/activate.ps1
```
When you have your enviorment running Remember to install all the dependencies with this command

```bash
  pip install -r requirements
```

Once that is done you are now ready to run the program.
Remember to cd to the folder that contains the .py files, here its :
```bash
  cd webscraper
```
## Running the program

Now you are all ready! Now run the script by typing in the terminal

```bash
  python main.py "<your-prompt-here>"
```