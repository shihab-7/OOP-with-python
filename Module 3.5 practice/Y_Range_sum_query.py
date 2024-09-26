size,querry = map(int,input().split())
A = list(map(int,input().split()))


prefix_sum = [0]* (size+1)
for i in range(1,size+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]

while querry != 0 :
    l , r = map(int,input().split())
    query_sum = prefix_sum[r] - prefix_sum[l-1]
    print(query_sum)
    querry-=1
