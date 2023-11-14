# ELFReader: simple ELF reader

This utility serves to print ELF code sgment headers and (optionally) data.


## Installation

pip install ELFReader-0.1.tar.gz


## Usage of ELFReader class

The only class ELFReader has two parameters:

* elf\_file: (str) pyth to the elf file
* flag\_print\_data: (bool) Whether print also the segment data, not only headers 


## Example

import ELFReader

er = ELFReader.ELFReader("file.elf", False)

er.read()
