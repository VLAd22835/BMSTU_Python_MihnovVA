from math import sin, cos, tan

def function_1(alfa):
    return (2*cos(alfa)*sin(2*alfa)-sin(alfa)/cos(alfa)-2*sin(alfa)*sin(2*alfa))

def function_2(alfa):
    return (tan(3*alfa))

with (open("input.txt", "r") as input_file):
    with open("output.txt", "w") as output_file:
        headr = "   alfa        y1          y2"
        print(headr)
        output_file.write(headr + "\n")
        for line in input_file:
            alfa_s = line.strip()
            if alfa_s:
                alfa = float(alfa_s)

                y1 = function_1(alfa)
                y2 = function_2(alfa)


            output_line = "{0: 7.2f}    {1:7.2f}    {2:9.4f}".format (alfa, y1, y2)

            print (output_line)
            output_file.write(output_line + "\n")
