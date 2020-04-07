'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''

# 1. virtual_test python3 -m venv second_venv
# 2. virtual_test source second_venv/bin/activate
# 3. (second_venv) ➜  virtual_test pip install django
# 4. (second_venv) ➜  virtual_test pip install --upgrade pip
# 5. (second_venv) ➜  virtual_test pip install pyroids
# 6. (second_venv) ➜  virtual_test pip freeze
     # asgiref==3.2.7
     # Django==3.0.5
     # pyglet==1.5.3
     # pyroids==0.9.0
     # pytz==2019.3
    # sqlparse==0.3.1
# 7. (second_venv) ➜  virtual_test pip freeze > requirements.txt
# 8. (second_venv) ➜  virtual_test deactivate
# 9. virtual_test rm -rf second_venv/
# 10. pip install -r /Users/Michael/Documents/CodingNomads_Python/virtual_test/requirements.txt

