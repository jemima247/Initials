matrix = [[2,4,6,8],[3,5,6,9],[1,3,5,2],[4,5,7,1]]
quote = ""

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        quote = quote + str(matrix[i][j])+ " " 
    
    quote = quote + "\n"

print(quote)

def sumCol(matrix):
    sumC = 0
    a = 1
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(a-1,a):
                print(matrix[i][j])
                sumC = sumC + matrix[i][j] 
            
        print(sumC)
        sumC = 0
        a = a + 1
        
    
sumCol(matrix)
