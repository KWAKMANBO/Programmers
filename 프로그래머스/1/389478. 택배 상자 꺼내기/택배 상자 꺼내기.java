import java.util.ArrayList;

class Solution {
        public int solution(int n, int w, int num) {
        int answer = 0;
        boolean direction = true;
        ArrayList<ArrayList<Integer>> board = new ArrayList<>();


        for (int i = 0; i < w; i++) {
            board.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < n; i++) {
            if(i % w == 0 && i != 1 && i != 0){
                direction = !direction;
            }

            if (direction) {
                board.get(i % w).add(i + 1);
            } else {
                board.get(w - 1 - i % w).add(i + 1);
            }
        }
   
        for(ArrayList<Integer> arr : board){
            if(arr.contains(num)){
                int idx = arr.indexOf(num);
                answer = arr.subList(idx,arr.size()).size();
            }
        }
        return answer;
    }
}