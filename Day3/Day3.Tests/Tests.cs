using Day3;
using FluentAssertions;

namespace Day5.Tests
{
    public class Tests
    {
        private const string engineSchematicStr = @"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        [Fact]
        public void Test_Part_1_Solution()
        {
            var engineSchematic = new EngineSchematic(engineSchematicStr);
            engineSchematic.GetSumOfPartNumbers().Should().Be(4361);
        }

        [Fact]
        public void Test_Part_2_solution() 
        {
            var engineSchematic = new EngineSchematic(engineSchematicStr);
            engineSchematic.GetSumOfGearRatios().Should().Be(467835);
        }
    }
}