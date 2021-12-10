def table(data):
    print(f"Date  |  Amount  |  Category  |  Description")
    for item in data:
        print(f"{item[0]}  |  {item[1]}  |  {item[2]}  |  {item[3]}")
