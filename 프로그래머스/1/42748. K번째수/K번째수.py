def solution(array, commands):
    #print(len(commands))
    answer= []
    for i in commands:
        #print(type(i))
        step = []
        for j in range(i[0],i[1]+1):
            print(j)
            step.append(array[j-1])
            step.sort()
        print(step)
        answer.append(step[i[2]-1])
        print(answer)
            #step.clear()
    return answer