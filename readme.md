# Install

* Clone de repo

```
git clone https://github.com/nildiert/concatenate_excel_files.git && cd concatenate_excel_files
```

* create a virtual env

```
python3 -m venv env
```

* Activate the environment 

```
source env/bin/activate
```

* Install dependencies

```
pip3 install -r requirements.txt
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