namespace Day4
{
    public class Scratchcard
    {
        public int CardNumber { get; set; }
        public IEnumerable<int> WinningNumbers { get; set; }
        public IEnumerable<int> NumbersWeHave { get; set; }

        public Scratchcard(string input) 
        {
            CardNumber = GetCardNumber(input);
            var numbers = input.Split(":")[1].Trim().Split('|');
            WinningNumbers = ParseNumbers(numbers[0].Trim());
            NumbersWeHave = ParseNumbers(numbers[1].Trim());
        }

        private IEnumerable<int> ParseNumbers(string numberList)
            => numberList.Split(' ', '\t')
                .Where(x => !String.IsNullOrWhiteSpace(x))
                .Select(int.Parse).ToList();

        public int CalculateScore() 
            => (int)Math.Pow(2, NumberOfWins() - 1);

        public int NumberOfWins()
            => NumbersWeHave
                .Count(x => WinningNumbers.Contains(x));

        private int GetCardNumber(string input) 
        {
            var cardNumberString = String.Join("", input.Split(":")[0].Trim().ToCharArray().Skip(4).ToArray());
            return int.Parse(cardNumberString);
        }

        public bool GeneratesCopyOf(int cardNumber) 
            => cardNumber > CardNumber && NumberOfWins() >= cardNumber - CardNumber;
    }
}
