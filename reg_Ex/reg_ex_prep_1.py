# import re

# log_Data = """
# [102.45] CPU0: Temp=72C, Freq=2400MHz
# [105.12] CPU0: Temp=88C, Freq=2100MHz
# [108.33] CPU0: Temp=92C, Freq=1800MHz
# """
# # Pattern logic: 
# # \[([\d.]+)\] -> Captures timestamp inside brackets
# # .*Temp=(\d+)C -> Skips to Temp value
# # .*Freq=(\d+)MHz -> Skips to Freq value
# pattern = r"\[([\d.]+)\] .*Temp=(\d+)C. Freq=(\d+)MHz"
# matches = re.findall(pattern, log_Data)
# print("Critical thermal Events:")
# for ts, temp, freq in matches:
#     if int(temp) >85:
#         print(f"Time: {ts}s | Temp: {temp}C | Freq: {freq}Mhz")

# import re
# addresses = ["0x1A2B3C4D", "0xG1234567", "1A2B3C4D", "0xBC4D", "0xabcdef01"]
# # ^0x -> Starts with 0x
# # [0-9a-fA-F]{8} -> Exactly 8 characters from 0-9 or A-F
# # $ -> End of string
# hex_pattern = r"^0x[0-9a-fA-F]{8}$"
# for addr in addresses:
#     if re.match(hex_pattern, addr):
#         print(f"VALID:{addr}")
#     else:
#         print(f"INVALID: {addr}")


# import re
# log = "PowerState_Change: CPU_Cluster_0 -> Deep_Sleep [Success]"
# pattern = r"PowerState_Change: (?P<comp>\w+) -> (?P<state>\w+) \[(?P<status>\w+).*\]"
# match =re.search(pattern, log)
# if match:
#     data = match.groupdict()
#     print(f"Component: {data['comp']}")
#     print(f"Attempted State: {data['state']}")
#     print(f"Result: {data['status']}")

    #re.search  and re.match remember that match() only checks the beginning of the string, while search() scans the entire string