/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int max=0;
    public int diameterOfBinaryTree(TreeNode root) {
        fun(root);
        return max;
    }
            private int fun(TreeNode root){
            if (root==null){
                return -1;
            }
            int left=fun(root.left);
            int right=fun(root.right);
            max=Math.max(max,2+left+right);
            return 1+Math.max(left,right);
        }
}
