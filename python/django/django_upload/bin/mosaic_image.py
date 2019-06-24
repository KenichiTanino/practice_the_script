#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys,os
from os import path, pardir

current_dir = path.abspath(path.dirname(__file__))
parent_dir = path.abspath(path.join(current_dir, pardir)) 
sys.path.append(parent_dir)

from libs.mosaic import MosaicFaceImage


@click.command()
@click.option('--file', '-f', type=str, default=None)
def mosaic(file):
    if not file:
        click.echo("file not found")
        exit(1)

    outfile = path.join(parent_dir, 'tmp', 'image.jpg')
    MosaicFaceImage().mosaic(file, outfile)


def main():
    mosaic()


if __name__ == '__main__':
    main()
