/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     long val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head= new ListNode(0) , p=head;
        int car=0;
        while(l1!=null || l2!=null || car!=0){
            int sum=car;
            if(l1!=null){
                sum+=l1.val;
                l1=l1.next;
            }
            if(l2!=null){
                sum+=l2.val;
                l2=l2.next;
            }
            p.next=new ListNode(sum%10);
            p=p.next;
            car=sum/10;
        }
        return head.next;
        }
}
