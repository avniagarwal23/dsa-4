// this function for checking valid palindrome
function checkPalindrome(str) {
    return str == str.split('').reverse().join('');
}

const string = "test"; 
const result = checkPalindrome(string);  
console.log(result);
