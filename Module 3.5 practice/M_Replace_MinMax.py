size = input()
elements = list(map(int,input().split()))

max_elm = elements.index(max(elements))
min_elm = elements.index(min(elements))

elements[min_elm],elements[max_elm] = elements[max_elm],elements[min_elm]

print(*elements)