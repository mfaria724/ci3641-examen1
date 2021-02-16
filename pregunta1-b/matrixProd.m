function prod = matrixProd(a,b)
  ##  assumes size is correct
  [x, y] = size(a);
  [w, z] = size(b);
  
  ## initializes result matrix
  prod = zeros(y);
  
  for i=1:x;
    for j=1:z;
      for k=1:y;
       prod(i, j) = prod(i, j) + a(i, k) * b(k, j);
      endfor
    endfor
  endfor
endfunction
