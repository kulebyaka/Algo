using System;
using System.Linq;

namespace ConsoleApp.Models
{
	public interface IContainer<T> where T : struct
	{
		public T Value { get; set; }
	}
}