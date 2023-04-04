import re 

def get_monkey_info(Lines):

    current_monkey = []
    monkey_data = []
    reading_monkey = False

    for line in Lines:

        if re.search("Monkey [0-999]{1}:", line):
            # reading a new monkey!
            # important information should be extracted!

            current_monkey = []

            current_monkey.append([re.findall("[0-999]", line)[0]])
            
            reading_monkey = True
        
        if (line == "\n") or (line == ""):

            reading_monkey == False
            monkey_data.append(current_monkey)

        elif reading_monkey == True:

            # get info from this line

            if "Starting items" in line:
                # get starting items
                # "Starting items: 79, 98"
                current_monkey.append(re.findall("([0-999]+)", line))

            elif "Operation" in line: 
                # get operation
                # "Operation: new = old * 19"
                op = line[23:24]

                if "old" in line[22:]:
                    # "old op old"
                    num = line[25:28]
                
                else:
                    # "old op (integer)"
                    num = line[25:len(line)].replace(" ", "").replace("\n", "")

                current_monkey.append([op, num])

            elif "Test" in line:
                # retrieve test
                # "Test: divisible by 23"

                current_monkey.append(re.findall("([0-999]+)", line))
            
            elif "If true" in line or "If false" in line:
                # retrieve monkey index
                # "If true: throw to monkey 2"
                # "If false: throw to monkey 3"
                current_monkey.append(re.findall("([0-999]+)", line))

    if current_monkey != []:
        # append last monkey If needed
        monkey_data.append(current_monkey)

    return monkey_data