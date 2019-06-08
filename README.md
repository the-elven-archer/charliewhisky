# CharlieWhisky

Morse code encoder and player for Python.  

## Installation

```
$ pip3 install git+https://github.com/the-elven-archer/charliewhisky.git
```

## Usage:

The library usage is very easy:

```python
from CharlieWhisky import CharlieWhisky

c = CharlieWhisky(debug=True, dit_duration_ms=100, frequency=600.0, samplerate=22050)

c.play_word("CQ CQ CQ DE LU1EXA LU1EXA K")
C -.-.
Q --.-

C -.-.
Q --.-

C -.-.
Q --.-

D -..
E .

L .-..
U ..-
1 .----
E .
X -..-
A .-

L .-..
U ..-
1 .----
E .
X -..-
A .-

K -.-
```
You should be hearing the *dits* and *dahs* on your soundcard.  
