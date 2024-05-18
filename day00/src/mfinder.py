import re

if re.fullmatch("[*][^*]{3}[*]", input()):
    if re.fullmatch("[*]{2}[^*][*]{2}", input()):
        if re.fullmatch("[*][^*][*][^*][*]", input()):
            print("True")
            exit()
print("False")


# cat tests/m_true.txt | python3 mfinder.py
# cat tests/m1_false.txt | python3 mfinder.py
# cat tests/m2_false.txt | python3 mfinder.py
