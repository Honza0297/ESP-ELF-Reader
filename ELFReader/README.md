# ELFReader: simple ELF reader

This utility serves to print ELF code sgment headers and (optionally) data.

## Usage

The only class ELFReader has two parameters:

* elf\_file: (str) pyth to the elf file
* flag\_print\_data: (bool) Whether print also the segment data, not only headers 


## Example

import ELFReader

er = ELFReader.ELFReader("blink.elf", False)

er.read()
