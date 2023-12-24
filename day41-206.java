/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev=null,temp=head,n=head;
        if(head==null)
            return head;
        while(temp.next!=null){
            n=temp.next;
            temp.next=prev;
            prev=temp;
            temp=n;
        }
        head=temp;
        head.next=prev;
        return head;
    }
}
