while(1):
    N = int(input())
    sum = 0
    number = []
    
    if(N == -1):
        break
        
    for i in range(1,N):
        if((N%i)==0): #i가 n의 약수일 경우
            sum += i #sum에 i 더함 
            number.append(i)
            
    if(N == sum): #n과 sum이 같을 경우 
        print(str(N) +" = ", end = '') 
        for idx,value in enumerate(number):
            if(idx != (len(number) -1)):
                print(str(value) + " + " ,end = '')
            else:
                print(str(value))
    else:
        print(str(N) + " is NOT perfect.")
            