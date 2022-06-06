need to install pytube

cmd - pip install pytube

BUGS fix

if pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
    cipher.py in line in 30
    var_regex = re.compile(r"^\w+\W")
    replace with var_regex = re.compile(r"^\w+\W")

if pytube.exceptions.VideoUnavailable: This video is unavailable ,
run this two cmd :
    python -m pip uninstall pytube pytube3 pytubex pytube4,
    python -m pip install pytube,
