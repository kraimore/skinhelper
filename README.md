# Simple python scripts to help with the skinning process

# Multiplier

Multiplies images with or without given syntax, i.e. followpoint-0, followpoint-1 etc.

## Usage

```
python3 multiplier.py -i [input]  -n [image count]
```
Example

```
python3 multiplier.py -i C:\Users\user\Pictures\fp.png -n 5 -f 3 -o followpoint-
```

## Arguments
```
-h | --help
-i | --input   [input]
-o | --output  [output syntax]
-n | --number  [image count]
-f | --first   [number of the first img (default: 0)]
```

# Downsizer

Downsizes HD skins (@2x elements) into SD skins.

## Usage

```
python3 downsizer.py -i [input]
```

Example

```
python3 downsizer.py -i C:\Users\user\osu!\skins\skin\
```

## Arguments
```
-h | --help
-i | --input   [input]
```
