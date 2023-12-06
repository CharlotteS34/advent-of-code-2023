
namespace Day3
{
    public class EngineSchematic
    {
        public EngineSchematic(string engineSchematic) 
        {
            _characters = engineSchematic
                .Split(Environment.NewLine)
                .Select(x => x.ToCharArray()
                .Select(y => y.ToString())
                .ToArray())
                .ToArray();
        }

        private readonly string[][] _characters;
        private int rowCount => _characters.Count();
        private int columnCount => _characters[0].Length;
        private static bool IsSymbol(string character)
            => character != "." && !int.TryParse(character, out var val);
        private static bool IsGearSymbol(string character)
            => character == "*";

        private IEnumerable<PotentialPartNumber> GetPotentialPartNumbers() 
        {
            var potentialPartNumbers = new List<PotentialPartNumber>();
            for (var i = 0; i < _characters.Length; i++) 
            {
                for (var j = 0; j < _characters[i].Length; j++) 
                {
                    if (int.TryParse(_characters[i][j], out var val))
                    {
                        var potentialPartNumber = new PotentialPartNumber();
                        var potentialPartNumberPositions = new List<Position>();
                        var k = j;
                        while (k < columnCount && int.TryParse(_characters[i][k], out var val2)) 
                        {
                            potentialPartNumber.NumberString += _characters[i][k];
                            potentialPartNumberPositions.Add(new Position(i, k));
                            k++;
                        }
                        potentialPartNumber.Positions = potentialPartNumberPositions;
                        j = k;
                        potentialPartNumbers.Add(potentialPartNumber);
                    }
                    else 
                    {
                        continue;
                    }
                }
            }
            return potentialPartNumbers;
        }

        private bool IsPartNumber(PotentialPartNumber potentialPartNumber) 
        {
            var positionsToCheck = potentialPartNumber.Positions
                .SelectMany(x => x.GetAdjacentPositions(rowCount, columnCount));
            return positionsToCheck.Any(pos => IsSymbol(_characters[pos.Row][pos.Column]));
        }

        private IEnumerable<int> GetPartNumbers()
            => GetPotentialPartNumbers().Where(IsPartNumber)
            .Select(x => x.Number);

        public int GetSumOfPartNumbers()
            => GetPartNumbers().Sum();

        private IEnumerable<Position> GetPotentialGearPositions() 
        {
            var positions = new List<Position>();
            for (var i = 0; i < rowCount; i++) 
            {
                for (var j = 0; j < _characters[i].Count(); j++) 
                {
                    if (IsGearSymbol(_characters[i][j])) 
                    {
                        positions.Add(new Position(i, j));
                    }
                }
            }
            return positions;
        } 

        public int GetSumOfGearRatios()
        {
            var sum = 0;
            var potentialPartNumbers = GetPotentialPartNumbers();
            var potentialGearPositions = GetPotentialGearPositions();
            foreach (var potentialGearPosition in potentialGearPositions)
            {
                var adjacentPartNumbers = potentialPartNumbers.Where(x => x.Positions.Any(y => y.IsAdjacentTo(potentialGearPosition)));
                if (adjacentPartNumbers.Count() == 2)
                {
                    sum += adjacentPartNumbers.Select(x => x.Number).Multiply();
                }
            }
            return sum;
        }
    }
}
