public class MinimumEvenMultiple {
    public MinimumEvenMultiple(){};
    public int returnSolution(int n){
        if(n%2 == 0) return(n);
        else return(n*2);
    }
    public static void main(String[] args) {
        MinimumEvenMultiple s = new MinimumEvenMultiple();
        System.out.println(s.returnSolution(15));
    }
}
