/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let ans = [];
    for (var i = 0; i < arr.length; i ++){
        let res = []
        let temp = 0;
        while (i < arr.length && temp < size){
            temp += 1
            res.push(arr[i])
            i += 1
        }
        if (temp <= size){
            ans.push(res)
            res = []
            temp = 0 
            i -= 1
        }
    }
    return ans 
};
