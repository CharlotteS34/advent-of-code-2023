using Day4;
using FluentAssertions;

namespace Day4Tests
{
    public class Tests
    {
        [Theory]
        [InlineData("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8)]
        [InlineData("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2)]
        [InlineData("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2)]
        [InlineData("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1)]
        [InlineData("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0)]
        [InlineData("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0)]
        public void Test_Part_1_Solution(string input, int expectedOutput) 
        {
            var scratchcard = new Scratchcard(input);
            scratchcard.CalculateScore().Should().Be(expectedOutput);
        }

        [Fact]
        public void Test_Part_2_Solution() 
        {
            var input = @"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";
            var lines = input.Split(Environment.NewLine);
            var scratchcards = lines.Select(line => new Scratchcard(line));
            var collection = new ScratchcardCollection(scratchcards);
            collection.CalculateScratchcardCount().Should().Be(30);
        }
    }
}
