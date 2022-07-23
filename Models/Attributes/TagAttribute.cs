using System;
using System.Collections.Generic;
using System.Linq;

namespace Models.Attributes
{
	// DataStructure attribute
	public class TagAttribute : Attribute
	{
		public TagAttribute(Tags[] values)
		{
			Values = values.ToList();
		}

		private List<Tags> Values { get; set; }
	}

	public enum Tags
	{
		BinaryTree,
		BinarySearchTree,
		LinkedList,
		Array,
		Stack,
		Queue,
		Heap,
		Tree,
		Graph,
		GraphSearch,
		Traversal,
		Math,
		String,
	}
}