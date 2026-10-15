/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const ans = {}
    for (let i = 0; i < this.length; i += 1){
        const key = fn(this[i])

        if (!ans[key]) {
            ans[key] = [];
        }

        ans[key].push(this[i]);

    }



    return ans 
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */