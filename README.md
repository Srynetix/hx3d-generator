# README #

Using this generator, you can easily start a project with the [**hx3d framework**](https://github.com/Srynetix/hx3d-framework) and a working game.  
The generator is written in Python, and use the Colorama library by Jonathan Hartley for color display.

## Configuration ##

You can configure certain aspects in the file `config.py` as:
- Android SDK directory
- hx3d Framework repository

## Using ##

You need to pass 3 arguments.
- `game`: The game name (e.g. "Hello")
- `destination`: The project directory (e.g. "some_random_folder") **(the folder must not exists !)**
- `package`: The package name (for android) (e.g. "org.test.app")

```
usage: generate.py [-h] [--new game destination package]

Generate a hx3d template

optional arguments:
  -h, --help            show this help message and exit
  --new game destination package
                        Generate a new game
```
