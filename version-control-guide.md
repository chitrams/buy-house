

1. Create new repository on GitHub
2. Clone repository to local machine:
```
git clone <repository-url>
cd mortgage-calculator
```
3. Set up virtual environment
```
conda create --name mortgage-calculator-env python=3.8
conda activate mortgage-calculator-env
```
4. Set up Python project
5. Initialise Git in project
```
git init
git add .
git commit -m "Initial commit"
```
6. Connect to GitHub
```
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

7. Making changes and committing
```
git add .
git commit -m "Your commit message"
git push origin main
```