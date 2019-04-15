# ScanQLi

SQLi scanner.

Tested on:
* Debian 9

### Installing

1. Install git tool
```
apt update
apt install git
```

2. Clone the repo.
```
git clone https://github.com/bambish/ScanQLi
```

3. Install python required libs
```
apt install python-pip
cd ScanQLi
pip install -r requirements.txt
```
_For python3 please install **python3-pip** and **pip3**_

### Usage

```
./scanqli -u [URL] [OPTIONS]
```

### Examples

Simple url scan with output file
```
python scanqli.py -u 'http://127.0.0.1/test/?p=news' -o output.log
```

Recursive URL scanning with cookies
```
python scanqli.py -u 'https://127.0.0.1/test/' -r -c '{"PHPSESSID":"4bn7uro8qq62ol4o667bejbqo3" , "Session":"Mzo6YWMwZGRmOWU2NWQ1N2I2YTU2YjI0NTMzODZjZDVkYjU="}'
```