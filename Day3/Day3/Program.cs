// See https://aka.ms/new-console-template for more information
using Day3;

Console.WriteLine("Hello, World!");
using (var reader = new StreamReader(@"C:\Code\Fun\advent-of-code-2023\Day3\input.txt")) 
{
    var engineSchematicString = reader.ReadToEnd();
    var engineSchematic = new EngineSchematic(engineSchematicString);
    Console.WriteLine($"Puzzle 1 solution {engineSchematic.GetSumOfPartNumbers()}");
    Console.WriteLine($"Puzzle 2 solution {engineSchematic.GetSumOfGearRatios()}");
}
