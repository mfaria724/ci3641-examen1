function factorial = fact(n)
    ## defined exactly as mathematical notation
    if (n == 0)
      factorial = 1
    else
      factorial = n * fact(n-1)
    endif
end