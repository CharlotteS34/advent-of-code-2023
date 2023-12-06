namespace Day3
{
    public static class NumericEnumerableExtensions
    {
        public static int Multiply(this IEnumerable<int> numbers)
            => numbers.Aggregate((x, y) => x * y);
    }
}
