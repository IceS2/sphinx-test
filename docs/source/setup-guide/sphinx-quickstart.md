# How to start documenting with Sphinx

## Installing sphinx

`pip install sphinx`

## Sphinx Quickstart

A good way to start is actually running `sphinx-quickstart docs`. This command will prompt you with a few questions to setup the `docs` folder with a default sphinx configuration.

- **Separate source and build directories (y/n) [n]:** Write "y" (Without quotes) and press Enter
- **Project name:** Write the name of your project and press Enter.
- **Author name(s):** Write the name of the responsible team and press Enter.
- **Project release []:** Write “0.1” (without quotes) and press Enter.
- **Project language [en]:** Leave it empty (the default, English) and press Enter.

## Understanding conf.py

You should now have a `docs/source/conf.py` file. This is where the Sphinx configuration is defined.
We will define the extensions to use, how to configure publishing the documentation to confluence and the theme. For now we can leave the default values (=
