fib := method(num,
  if(num < 2, return num)

  return fib(num - 1) + fib(num - 2)
)

Foo := Object clone
Foo calc_fib := method(num,
  if(num < 2, return num)

  return fib(num - 1) + fib(num - 2)
)


Foo getSlot("calc_fib") println
