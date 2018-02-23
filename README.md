# helloworld
Helloworld package


#Installing the package 

Clone and install the package

```python
git clone https://github.com/mvanack/helloworld.git
cd helloworld/
pip install .
```

## CLI Usage 

### To use the executable command line program:

```python
$ helloworld -h
usage: helloworld [-h] [-n NAME] [--popcorn] [--countdown]

required arguments:
--countdown = integer  countdown needs to be set with a negative or positive integer value.

optional arguments:
-h, --help				show the help message 
-n NAME, --name NAME 	optional name to say hello to 	
--popcorn 				print movie
--countdown = int		prints showtime or snack time depending on integer value
```
## API Usage 

To use the helloworld Python API:
```python 
import helloworld
helloworld.helloworld(name="Meredith")   	 
```