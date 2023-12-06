namespace Day4
{
    public class ScratchcardCollection
    {
        public ScratchcardCollection(IEnumerable<Scratchcard> scratchcards) 
        {
            Scratchcards = scratchcards.ToArray();
        }
        public IEnumerable<Scratchcard> Scratchcards { get; set; }

        public int CalculateScratchcardCount()
        => Scratchcards.Select(x => CalculateCopiesOf(x.CardNumber))
            .Sum();

        private int CalculateCopiesOf(int cardNumber) 
        {
            var scratchcardsWhichGenerateCopies = Scratchcards.Where(scr => scr.GeneratesCopyOf(cardNumber));
            return  1 + scratchcardsWhichGenerateCopies.Select(scratchcard => CalculateCopiesOf(scratchcard.CardNumber)).Sum();
        }
    }
}
