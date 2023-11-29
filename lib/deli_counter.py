def line(deli_line):
    # displays the current line of customers waiting to be served
    if len(deli_line) == 0:
    # handle conditon when line is empty
        print('The line is currently empty.')
    else:
    # construct the line string
        line_string = 'The line is currently: '
        for index, person in enumerate(deli_line):
            if index == len(deli_line) - 1:
    # don't add a space after the last person's name
                line_string += f'{index + 1}. {person}'
            else:
    # append each person's name and position
                line_string += f'{index + 1}. {person} '
    # print the final string
        print(line_string)

def take_a_number(deli_line, new_customer):
    # adds a new customer to the end of the line and assign their position
    position = len(deli_line) + 1
    # calculate the new customer's position
    deli_line.append(new_customer)
    # add the new customer to the line
    print(f'Welcome, {new_customer}. You are number {position} in line.')
    # print welcome message

def now_serving(deli_line):
    # removes and serves the first customer in line
    if len(deli_line) == 0:
    # handle the condition when line is empty
        print('There is nobody waiting to be served!')
    else:
    # remove and store the current customer
        current_customer = deli_line.pop(0)
    # print message indicating who is currently being served
        print(f'Currently serving {current_customer}.')