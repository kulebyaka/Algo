using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

// tasks and enumerable tricks
IEnumerable<Task> taskStars = new[]
{
	Task.Run(() => Console.Write("*")),
	Task.Run(() => Console.Write("*")),
};
await Task.WhenAll(taskStars);
Console.WriteLine($"{taskStars.Count()} stars!");

IEnumerable<Task> tasksAmpersands = Enumerable.Range(0, 2).Select(_ => Task.Run(() => Console.Write("&")));
await Task.WhenAll(tasksAmpersands);
Console.WriteLine($"{tasksAmpersands.Count()} ampersands!");