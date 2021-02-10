using System.Collections.Generic;

namespace Models.Structures.Tree
{
	public class TreeNode<T>:IContainer<T> where T : struct
	{
		public List<TreeNode<T>> Nodes { get; set; }
		public T Value { get; set; }
	}
}