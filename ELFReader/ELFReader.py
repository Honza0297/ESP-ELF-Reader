from elftools.elf.elffile import ELFFile
import argparse

class ELFReader:
    """
    ELFReader class, providing interface for printing all program segments.
    """
    def __init__(self, elf_file, flag_print_data):
        self.file = elf_file
        self.flag_print_data = flag_print_data
        self.elf_file = None

    def read(self):
        elf_file = open(self.file, 'rb')
        self.elf_file = ELFFile(elf_file)
        segments = [segment for segment in self.elf_file.iter_segments() if segment['p_type'] == 'PT_LOAD' and segment['p_flags'] & 0x1]
        for idx, segment in enumerate(segments):
            print("Header {}:".format(idx))
            self.print_header(segment)
            print("")
            if self.flag_print_data:
                print("Data:")
                print(segment.data())
        elf_file.close()

    def print_header(self, segment):
        print("->Segment Type: {}".format(segment['p_type']))
        print("->Offset in File: {}".format(hex(segment['p_offset'])))
        print("->Virtual Address: {}".format(hex(segment['p_vaddr'])))
        print("->Physical Address: {}".format(hex(segment['p_paddr'])))
        print("->Segment Size in File: {} bytes".format(segment['p_filesz']))
        print("->Segment Size in Memory: {} bytes".format(segment['p_memsz']))
        print("->Segment Flags: {}".format(hex(segment['p_flags'])))
        print("->Alignment: {}".format(segment['p_align']))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="ELF file with data")
    parser.add_argument("-p", "--print_data", type=bool, help="Specify if print data or only headers", default="False")
    args = parser.parse_args()

    reader = ELFReader(elf_file=args.file, flag_print_data=False)
    reader.read()