using System.Collections.Generic;

namespace ConsoleApp.Models.Tree
{
	public class TreeNode<T>:IContainer<T> where T : struct
	{
		public List<TreeNode<T>> Nodes { get; set; }
		public T Value { get; set; }
	}
}