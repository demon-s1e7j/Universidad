-- factorial :: Int -> Int
-- factorial 0 = 1
-- factorial n =  n * factorial(n - 1)
productFromTo :: Int -> Int -> Int
productFromTo a b = 
  if a > b then 1
  else if a == b then a
  else productFromTo a c * productFromTo (c + 1) b
  where c = (a + b) `div` 2

-- factorial :: None -> (Int -> Int)
factorial = productFromTo 1

main :: IO ()
main = do
  print (factorial 120)
