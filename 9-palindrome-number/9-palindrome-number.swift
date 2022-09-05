class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        var myString = String(x)
        var reversed = String(myString.reversed())
        if (myString==reversed){
            return true
        }
        else{
            return false
        }
    }
}