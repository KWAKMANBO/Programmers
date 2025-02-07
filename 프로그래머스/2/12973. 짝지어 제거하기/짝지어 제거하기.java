

import java.util.ArrayList;
class Solution
{
    public int solution(String s)
    {
        ArrayList<Character> stack = new ArrayList<>();

        for(int i= 0; i< s.length(); i++){
            if ( !stack.contains(s.charAt(i)) || stack.get(stack.size() - 1) != s.charAt(i)){
                stack.add(s.charAt(i));
            }else if (stack.get(stack.size()-1) == s.charAt(i)){
                stack.remove(stack.size()-1);
            }
        }

        return stack.isEmpty() ? 1 : 0;
    }
}