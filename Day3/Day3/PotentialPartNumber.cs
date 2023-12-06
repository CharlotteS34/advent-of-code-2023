namespace Day3
{
    public class PotentialPartNumber
    {
        public PotentialPartNumber() 
        {
            NumberString = "";
        }
        public string NumberString { get; set; }
        public int Number => int.Parse(NumberString);
        public IEnumerable<Position> Positions { get; set; }
    }
}
