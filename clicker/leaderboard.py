import csv

# Define the new row data
def leader(name, score, diff):
    new_row_data = [name, score, diff]  # Replace with your actual data

    # Specify the CSV file path
    csv_file_path = r'C:\Users\User\Desktop\botik\clicker\leaderboard.csv'  # Replace with your CSV file name

    with open(r'C:\Users\User\Desktop\botik\clicker\leaderboard.csv', newline='') as f:
        reader = csv.reader(f)
        print(reader)
        data = list(reader)
    for i in range(len(data)):
        data[i][0] = data[i][0].strip()
        data[i][1] = data[i][1].strip()
        data[i][2] = data[i][2].strip()
    print(data)
    if any(name in sublist for sublist in data):
        for i in range(len(data)):
            if data[i][0] == name:
                if score> int(data[i][1]):
                    data[i][1] = score                

    else:data.append(new_row_data)
    s = sorted(data, key= lambda x: int(x[1]),reverse = True)
    print(s)
    with open(csv_file_path, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for i in s:
            writer.writerow(i)
