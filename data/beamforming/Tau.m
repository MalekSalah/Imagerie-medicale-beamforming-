function t = Tau (x_i, x, z)
  global c
  t  = (z + sqrt(z^2 + (x - x_i)^2))/c
endfunction
