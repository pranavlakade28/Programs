
salaries=[45000.5,38000.5,52000.75,61000.0,47000.0,70000.0,56000.0,49000.5]
              
def selection_sort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
    return a

def bubble_sort(a):
    for i in range(len(a)):
      for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    return a

s1=salaries.copy()
selection_sort(s1)     
print("Top 5 Salaries using selection_sort:")
print(s1[-5:][::-1])
s2=salaries.copy()
bubble_sort(s2)
print("\nTop5 Salaries using Bubble Sort:")
print(s2[-5:][::-1])
   