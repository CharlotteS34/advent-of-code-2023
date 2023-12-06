// See https://aka.ms/new-console-template for more information
using Day4;

var file_lines = new List<string>();
using (var reader = new StreamReader(@"C:\Code\Fun\advent-of-code-2023\Day4\input.txt")) 
{
    while (!reader.EndOfStream) 
    {
        file_lines.Add(reader.ReadLine());
    }
}
var puzzle_1_solution = file_lines.Select(line =>
{
    var scratchcard = new Scratchcard(line);
    return scratchcard.CalculateScore();
}).Sum();
Console.WriteLine($"Puzzle 1 solution: {puzzle_1_solution}");

var scratchcards = file_lines.Select(line => new Scratchcard(line));
var scratchcardCollection = new ScratchcardCollection(scratchcards);
var puzzle_2_solution = scratchcardCollection.CalculateScratchcardCount();
Console.WriteLine($"Puzzle 2 solution: {puzzle_2_solution}");



