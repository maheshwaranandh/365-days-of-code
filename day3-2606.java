class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        Map<Character,Integer>hm=new HashMap<>();
        for(int i=0;i<chars.length();i++){
            hm.put(chars.charAt(i),vals[i]);
        }
        int res=0;
        int cur=0;
        for(int i=0;i<s.length();i++){
            cur+=hm.getOrDefault(s.charAt(i),s.charAt(i)-'a'+1);
            res=Math.max(res,cur);
            if(cur<0){
                cur=0;
            }
        }
    return res;
    }
}
