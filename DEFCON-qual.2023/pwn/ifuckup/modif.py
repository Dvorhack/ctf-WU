import lief

crackme101 = lief.parse("./ifuckup.so")

print(crackme101.header.file_type)

print(len(crackme101.exported_functions))

for func in crackme101.exported_functions:
    print(func)

# crackme101.add_exported_function(0xa41, "next_random")
# crackme101.write("ifuckup.so")


# crackme101[lief.ELF.DYNAMIC_TAGS.FLAGS_1].remove(lief.ELF.DYNAMIC_FLAGS_1.PIE)
# crackme101.write("verify" + ".patched")
