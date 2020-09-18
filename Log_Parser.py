filename = "NtPump.txt"
print("Enter the ID of interest: (hex format)")
ID_enter = input()
parsed = []
whitelist = [ID_enter]
with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    for ID in whitelist:
        if ID in line:
            parsed.append(line)

with open("log_parsed", "w") as fw_obj:
    fw_obj.writelines(parsed)
