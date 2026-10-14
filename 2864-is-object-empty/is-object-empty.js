/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (obj.length){
        return false
    }
    keys = Object.keys(obj)
    if (keys.length >  0){
        return false
    }
    return true
};