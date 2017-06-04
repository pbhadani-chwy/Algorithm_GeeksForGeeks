class node:
    def __init__ (self,no_of_zero,no_of_one):
        self.no_of_zero = no_of_zero
        self.no_of_one = no_of_one
        self.sum = self.no_of_zero - self.no_of_one



T = int(input())
while (T!=0):
    temp = []
    size = input()
    sampleIn = input()
    z = sampleIn.split()
    for i in range(len(z)):
        if i == 0:
            if (z[i] == '1'):
                temp.append(node(0,1))
            else:
                temp[i] = node(1,0)
        else:
            if (temp[i-1].sum <= 0):
                if (z[i] == '1'):
                    temp.append(node(0,1))
                else:
                    temp.append(node(1,0))
            else:
                if (z[i] == '1'):
                    temp.append(node(temp[i-1].no_of_zero,temp[i-1].no_of_one + 1))
                else:
                    temp.append(node(temp[i-1].no_of_zero + 1,temp[i-1].no_of_one))
    for i in range(len(temp)):
        print(temp[i].no_of_zero,temp[i].no_of_one,temp[i].sum)

    T -= 1
