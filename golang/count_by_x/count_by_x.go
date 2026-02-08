func CountBy(x, n int) []int {
  
  var arr1 []int
  
  for i := 1; i <= n; i++{
    arr1 = append(arr1, (i * x))
  }
  
  return arr1
}
