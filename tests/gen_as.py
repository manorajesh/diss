from riscv_assembler.convert import AssemblyConverter
cnv = AssemblyConverter()
cnv.convert("test.s") # outputs to binary file test.bin