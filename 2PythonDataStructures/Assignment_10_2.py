# Assignment 10.2
file_name = "mbox-short"
file_handler = open(file_name.lower() + ".txt", "r")
time_dict = dict()

for each_line in file_handler:
    if each_line.startswith("From") and not each_line.startswith("From:"):
        current_line = (each_line.split())
        current_time = current_line[5]
        current_hour_split = current_time.split(":")
        current_hour = current_hour_split[0]
        time_dict[current_hour] = time_dict.get(current_hour, 0) + 1


final_list = sorted((k, v) for k, v in time_dict.items())
for hours, count in final_list:
    print(hours, count)
