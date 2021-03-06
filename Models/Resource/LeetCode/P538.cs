﻿using System;
using Models.Attributes;
using Models.Structures.Tree;

namespace Models.Resource.LeetCode
{
	[BinaryTreeTag]
	public class P538
	{
		private int _counter = 0;
		public BinaryTreeNode<int> ConvertBST(BinaryTreeNode<int> node)
		{
			if (node!=null)
				InOrderLeftTraversal(node, (a, b)=>a.Value += b);
			return node;
		}
		
		public void InOrderLeftTraversal(BinaryTreeNode<int> node, Action<BinaryTreeNode<int>, int> visit)
		{
			void VisitOrNull(BinaryTreeNode<int> binaryTreeNode)
			{
				if (binaryTreeNode != null)
					InOrderLeftTraversal(binaryTreeNode, visit);
			}
			VisitOrNull(node.Right);
			visit(node, _counter);
			_counter = node.Value;
			VisitOrNull(node.Left);
		}
	}
}