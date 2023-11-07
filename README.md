# Use in VS Code

The project is using "Dev containers" VS code features. To use it, you need to install the "Dev Containers" extension.

Then, when you open the project in VS Code, you will be prompted to open the project in a container. Accept it and a new VS Code window will open with the project in a container. If you are not prompted, you can still open the command palette (Ctrl+Shift+P) and type "Dev-Containers: Reopen in Container" or "Dev-Containers: Rebuild and Reopen in Container".

**At that moment, you would be directly inside the container.**

# Interpreter

To be sure that vscode has selected the right interpreter (the one in the container), you can open the command palette (Ctrl+Shift+P) and type "Python: Select Interpreter".

To be sure to take the right one, open a terminal (Ctrl + ù) and type : 

```bash
poetry shell
which python
```

The output should be something like : 

```bash
/root/.cache/pypoetry/virtualenvs/xxx-xxx-py3.12/bin/python
```

You should see it in the list of available interpreters. If not, you can select it manually by typing the path in the input field.

# Extensions

Extensions listed in .devcontainer/devcontainer.json will be installed automatically.

NB: On first start, since "Python" extension can take longer time to install than mypy or Pylance one, you may have to restart VS Code (Ctrl+Shift+P, "Reload Window") to have them working properly. It would not happen again after that.

mypy and Ruff extensions are installed to help you, as you write code, to detect errors the earliest possible. You are free to disabled them if you want but you should also know that a github action is set to check that the code is mypy and ruff compliant before merging it to "main" and "dev" branches.

The choice to have a mypy/ruff check on a github actions instead of a pre-commit hook is to let you code as you want until you want to merge it to the main branch where then you would have to be conform to common conventions.