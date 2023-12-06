namespace Day3
{
    public class Position
    {
        public Position(int row, int column)
        {
            Row = row;
            Column = column;
        }

        public int Row { get; set; }
        public int Column { get; set; }

        private bool IsEqualTo(Position other)
            => other.Row == Row && other.Column == Column;

        public IEnumerable<Position> GetAdjacentPositions(int rowCount, int columnCount)
        {
            var positions = new Position[] 
            {
                new Position(Row - 1, Column - 1),
                new Position(Row - 1, Column),
                new Position(Row - 1, Column + 1),
                new Position(Row, Column - 1),
                new Position(Row, Column + 1),
                new Position(Row + 1, Column - 1),
                new Position(Row + 1, Column),
                new Position(Row + 1, Column + 1),
            };
            return positions
                .Where(x => x.Row >= 0 && x.Row < rowCount && x.Column >= 0 && x.Column < columnCount);
        }

        public bool IsAdjacentTo(Position other) 
            => !IsEqualTo(other) && other.Row >= Row - 1 && other.Row <= Row + 1 && other.Column >= Column - 1 && other.Column <= Column + 1;
    }
}