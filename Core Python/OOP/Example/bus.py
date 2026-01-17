# take li for location
# take li for distance
# finding index of s1
# src = s1
# dist = s3

# ind of src 
# ind of dest

# for i in range (i-srs,ind-dist)

# sum += dist[i]


# # i = i_src                                         
# # while(i!=i_dest)
# sum += dis[i]
# if(i == len(loc)-1):
#     i =0
                
# else:                    
#     i+=1                



loc = [1,2,3,4,5]
dist = [1000, 2000, 3000, 4000,5000]

ind_src = int(input('Enter Starting location :'))
ind_dest =int(input('Enter Ending location :'))

j = ind_src
sum = 0
while(j != ind_dest):
    if(j == len(loc)):
        j = 0
    else:
        j += ind_src
    sum += dist[j]

print(sum)
                                                                
                                                    
                                                                             
                                                                              
                                     
                                                         
                                         
                                         
                                                                                                                                                   
                                                                                                                                                                                                                     