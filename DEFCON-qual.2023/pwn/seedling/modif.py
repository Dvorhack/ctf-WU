import lief

crackme101 = lief.parse("./verify.patched")

print(len(crackme101.exported_functions))

for func in crackme101.exported_functions:
    print(func)

# crackme101[lief.ELF.DYNAMIC_TAGS.FLAGS_1].remove(lief.ELF.DYNAMIC_FLAGS_1.PIE)
# crackme101.write("verify" + ".patched")
