class Solution {
 public:
 bool checkString(string s) {
 for (int i = 0; i < s.length()-1; i++)    // we run a loop from starting till the end of loop
 {
    if (s[i] > s[i + 1])       //we check if character at i is greater than next character at i+1
    {
        return false;      // if the condition is true (only in case 'ba') then we return false
    }
 }
  
  return true;           //if we havent returned false yet its obvious that there is no case of ba in the string therefore we return true 

   }
 };