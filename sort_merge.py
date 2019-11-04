
# merge sort
def sort_merge_recursion(A, *, key=None, reverse=False):
         """
         Sort 'A' based on the values, 'A[i]' or 'key(A[i])' if the functions,
         'key' is given, in the descending ('reverse=True) or ascending
         ('reverse=False') order. If 'key=None', the values of 'A[i]'.
         -------
         Argument
         -:key: None or function to return a value used for comparison
         """
         def fMerge(A1, A2):
                  """
                  Merge the two sorted lists, 'A1' and 'A2' into one sorted
                  list and return it.
                  """
                  n1 = len(A1)
                  n2 = len(A2)
                  n = n1 + n2
                  B = [0]*n
                  i1 = 0
                  i2 = 0
                  i = 0
                  while i1 < n1 and i2 <n2:
                           if key is None:
                                    a1 = A1[i1]
                                    a2 = A2[i2]
                           else:
                                    a1 = key(A1[i1])
                                    a2 = key(A2[i2])
                           if reverse == True:
                                    if a1 >= a2:
                                             B[i] = A1[i1]
                                             i1 += 1
                                    else:
                                             B[i] = A2[i2]
                                             i2 += 1
                           else:
                                    if a1 > a2:
                                             B[i] = A2[i2]
                                             i2 += 1
                                    else:
                                             B[i] = A1[i1]
                                             i1 += 1
                           i += 1
                  B[i: ] = A2[i2: ] if i1 == n1 else A1[i1: ]
                  
                  return B
         
         n = len(A)
         if n == 2:
                  A = fMerge(A[:1], A[1:])
         elif n == 3:
                  A[:2] = fMerge(A[:1], A[1:2])
                  A = fMerge(A[:2], A[2:])
         
         elif n > 3:
                  A[:n//2] = sort_merge_recursion(A[:n//2], key=key, reverse=reverse)
                  A[n//2:] = sort_merge_recursion(A[n//2:], key=key, reverse=reverse)
                  A[:] = fMerge(A[:n//2], A[n//2:])
         # print(A)
         return A

def sort_merge_iteration(A, *, key=None, reverse=False):
         """
         Sort 'A' based on the values, 'A[i]' or 'key(A[i])' if the functions,
         'key' is given, in the descending ('reverse=True) or ascending
         ('reverse=False') order. If 'key=None', the values of 'A[i]'.
         -------
         Argument
         -:key: None or function to return a value used for comparison
         """
         def fMerge(A1, A2):
                  """
                  Merge the two sorted lists, 'A1' and 'A2' into one sorted
                  list and return it.
                  """
                  n1 = len(A1)
                  n2 = len(A2)
                  n = n1 + n2
                  B = [0]*n
                  i1 = 0
                  i2 = 0
                  i = 0
                  while i1 < n1 and i2 <n2:
                           if key is None:
                                    a1 = A1[i1]
                                    a2 = A2[i2]
                           else:
                                    a1 = key(A1[i1])
                                    a2 = key(A2[i2])
                           if reverse == True:
                                    if a1 >= a2:
                                             B[i] = A1[i1]
                                             i1 += 1
                                    else:
                                             B[i] = A2[i2]
                                             i2 += 1
                           else:
                                    if a1 > a2:
                                             B[i] = A2[i2]
                                             i2 += 1
                                    else:
                                             B[i] = A1[i1]
                                             i1 += 1
                           i += 1
                  B[i: ] = A2[i2: ] if i1 == n1 else A1[i1: ]
                  
                  return B
         
         n = len(A)
         i = 1
         while i < n:
                  i *= 2
                  for j in range(n//i + (n%i!=0)):
                           tempI = i*j
                           i_0 = i//2
                           A[tempI: tempI+i] = fMerge(A[tempI: tempI+i_0], A[tempI+i_0: tempI+i])
         

if __name__ == '__main__':
         import time
         reverse = True
         a = list(range(500000))
         start = time.time()
         a = sort_merge_recursion(a, reverse=reverse)
         print('Recursion Time: %0.3f'%(time.time() - start))
         a = list(range(500000))
         start = time.time()
         sort_merge_iteration(a, reverse=reverse)
         print('Iteration Time: %0.3f'%(time.time() - start))
         a = list(range(500000))
         start = time.time()
         a.sort(reverse=reverse)
         print('Built-in Time: %0.3f'%(time.time() - start))
