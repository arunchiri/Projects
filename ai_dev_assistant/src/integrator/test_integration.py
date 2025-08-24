import rpy2.robjects as robjects

# Initialize R
r = robjects.r

# Execute a simple R command
pi = r('pi')
print(f"The value of pi from R is: {pi[0]}")

# Define an R function and call it
r('''
add <- function(a, b) {
  return(a + b)
}
''')

add_func = robjects.globalenv['add']
result = add_func(5, 10)
print(f"The result of 5 + 10 from R is: {result[0]}")

print("Python-R integration test successful!")
