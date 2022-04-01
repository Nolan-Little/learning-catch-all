division := Number getSlot("/")

Number / := method(num,
  if(num == 0, 0, self division(num))
)

4 / 2 println
4 / 0 println
5 / 10 println