<img width="800" height="162" alt="image" src="https://github.com/user-attachments/assets/993ed96b-d2c5-4bef-abd7-dc6b81e442b8" />

# Assignment 2 – Continuous Integration with Azure DevOps

Student starter repository.

Contents:
- `app/hello.py` – small Python application
- `tests/test_hello.py` – automated tests
- `requirements.txt` – dependencies
- `azure-pipelines.yml` – incomplete CI pipeline

Complete the pipeline according to the assignment specification.

The final pipeline must:
1. Trigger on pushes to `main`.
2. Use `ubuntu-latest`.
3. Use Python 3.12.
4. Install dependencies.
5. Run automated tests.
6. Fail when tests fail.
7. Publish an artifact containing the application.

Use Azure CLI where appropriate and document your commands and screenshots in the report.
