# Install

* Clone de repo

```
git clone https://github.com/nildiert/concatenate_excel_files.git && cd concatenate_excel_files
```

* create a virtual env

```
python -m venv env
```

* Install dependencies

```
pip install -r requirements.txt
```

* Create data directory

```
mkdir data
```


* Storage all your .xlsx files in the data directory and execute the following script

```
ls data -a | sort > data.txt
```

* execute the script

```
./script.py
```